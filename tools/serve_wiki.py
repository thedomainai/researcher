#!/usr/bin/env python3
"""Serve the generated wiki locally without depending on stderr for logging."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import TextIO


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WIKI_DIR = REPO_ROOT / "wiki"
DEFAULT_LOG_FILE = REPO_ROOT / "logs" / "local-server.log"


def append_log(log_fp: TextIO | None, message: str) -> None:
    if log_fp is None:
        return
    try:
        log_fp.write(message + "\n")
        log_fp.flush()
    except OSError:
        # The server must keep serving even if the log sink disappears.
        pass


class ResilientRequestHandler(SimpleHTTPRequestHandler):
    """Simple handler that never lets logging failures break responses."""

    def __init__(self, *args, log_fp: TextIO | None = None, **kwargs):
        self._log_fp = log_fp
        super().__init__(*args, **kwargs)

    def log_message(self, format: str, *args) -> None:
        try:
            message = "%s - - [%s] %s" % (
                self.address_string(),
                self.log_date_time_string(),
                format % args,
            )
        except Exception:
            return
        append_log(self._log_fp, message)

    def log_error(self, format: str, *args) -> None:
        self.log_message(format, *args)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve the generated wiki locally in a robust way."
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to.")
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to bind to. Default: 8000."
    )
    parser.add_argument(
        "--directory",
        type=Path,
        default=DEFAULT_WIKI_DIR,
        help="Directory to serve. Default: repo/wiki.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=DEFAULT_LOG_FILE,
        help="Append-only log file. Default: logs/local-server.log.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    directory = args.directory.resolve()
    if not directory.is_dir():
        raise SystemExit(f"Directory does not exist: {directory}")

    log_path = args.log_file.resolve()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as log_fp:
        append_log(
            log_fp,
            f"Serving {directory} at http://{args.host}:{args.port}",
        )
        handler = partial(ResilientRequestHandler, directory=str(directory), log_fp=log_fp)
        with ThreadingHTTPServer((args.host, args.port), handler) as httpd:
            httpd.serve_forever()


if __name__ == "__main__":
    main()
