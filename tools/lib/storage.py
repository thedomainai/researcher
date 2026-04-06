"""Paper storage: save Markdown files and manage index.jsonl."""

import json
import os
from typing import Dict, List, Optional, Set

from .utils import slugify, title_hash
from .schema import build_markdown, build_index_entry


class PaperStore:
    """Manages paper Markdown files and the append-only index."""

    def __init__(self, base_dir):
        # type: (str) -> None
        self.base_dir = base_dir
        self.raw_papers = os.path.join(base_dir, "raw", "papers")
        self.raw_articles = os.path.join(base_dir, "raw", "articles")
        self.index_path = os.path.join(base_dir, "raw", "index.jsonl")
        self._hashes = None  # type: Optional[Set[str]]

    def load_existing_hashes(self):
        # type: () -> Set[str]
        """Load title hashes from index.jsonl for deduplication."""
        if self._hashes is not None:
            return self._hashes
        hashes = set()  # type: Set[str]
        if os.path.exists(self.index_path):
            with open(self.index_path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        t = entry.get("title", "")
                        if t:
                            hashes.add(title_hash(t))
                    except json.JSONDecodeError:
                        continue
        self._hashes = hashes
        return hashes

    def is_duplicate(self, title):
        # type: (str) -> bool
        """Check if a paper with this title already exists."""
        hashes = self.load_existing_hashes()
        return title_hash(title) in hashes

    def save_paper(self, paper_data, abstract="", dry_run=False):
        # type: (Dict, str, bool) -> Optional[str]
        """Save paper as Markdown file.

        Returns relative file path (e.g., "papers/domain/slug.md") on success,
        or None if duplicate or dry_run.
        """
        title = (paper_data.get("title") or "untitled").replace("\n", " ")
        domain = paper_data.get("domain", "unknown")

        # Deduplication
        th = title_hash(title)
        hashes = self.load_existing_hashes()
        if th in hashes:
            return None

        slug = slugify(title)
        rel_path = "papers/%s/%s.md" % (domain, slug)

        if dry_run:
            hashes.add(th)
            return rel_path

        domain_dir = os.path.join(self.raw_papers, domain)
        os.makedirs(domain_dir, exist_ok=True)
        filepath = os.path.join(domain_dir, "%s.md" % slug)

        # File-level dedup (slug collision)
        if os.path.exists(filepath):
            hashes.add(th)
            return None

        md_content = build_markdown(paper_data, abstract)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        hashes.add(th)
        return rel_path

    def append_to_index(self, entries):
        # type: (List[Dict]) -> None
        """Append entries to index.jsonl."""
        if not entries:
            return
        with open(self.index_path, "a", encoding="utf-8") as f:
            for entry in entries:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
