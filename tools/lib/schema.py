"""Unified frontmatter schema for paper Markdown files."""

from datetime import datetime
from typing import Dict, Optional


# Required fields (always output)
REQUIRED_FIELDS = [
    "title", "authors", "year", "citations",
    "paper_type", "domain", "domain_label",
    "source_api", "fetched",
]

# Conditional fields (always output, empty string if missing)
CONDITIONAL_FIELDS = [
    "doi", "openalex_id", "semantic_scholar_id", "arxiv_id", "url",
]

# Optional fields (output only when value is present)
OPTIONAL_FIELDS = [
    "tier", "influential_citations", "categories", "explore_depth",
]


def build_frontmatter(paper_data):
    # type: (Dict) -> str
    """Build YAML frontmatter string from paper data dict.

    paper_data should contain keys matching REQUIRED_FIELDS.
    Missing conditional fields default to empty string.
    Optional fields are only included when present and non-None.
    """
    lines = ["---"]

    # Required fields
    lines.append('title: "%s"' % _escape_yaml(paper_data.get("title", "untitled")))
    lines.append('authors: "%s"' % _escape_yaml(paper_data.get("authors", "")))
    lines.append("year: %s" % (paper_data.get("year", 0) or 0))
    lines.append("citations: %s" % (paper_data.get("citations", 0) or 0))
    lines.append('paper_type: "%s"' % paper_data.get("paper_type", "primary"))
    lines.append('domain: "%s"' % paper_data.get("domain", ""))
    lines.append('domain_label: "%s"' % paper_data.get("domain_label", ""))
    lines.append('source_api: "%s"' % paper_data.get("source_api", ""))
    lines.append('fetched: "%s"' % paper_data.get("fetched", datetime.now().isoformat()))

    # Conditional fields (always present, empty string if missing)
    for field in CONDITIONAL_FIELDS:
        val = paper_data.get(field, "")
        lines.append('%s: "%s"' % (field, _escape_yaml(str(val) if val else "")))

    # Optional fields (only when present and non-None)
    for field in OPTIONAL_FIELDS:
        val = paper_data.get(field)
        if val is not None:
            if isinstance(val, str):
                lines.append('%s: "%s"' % (field, _escape_yaml(val)))
            else:
                lines.append("%s: %s" % (field, val))

    lines.append("---")
    return "\n".join(lines)


def build_markdown(paper_data, abstract=""):
    # type: (Dict, str) -> str
    """Build complete Markdown file content for a paper."""
    frontmatter = build_frontmatter(paper_data)
    title = paper_data.get("title", "untitled")
    authors = paper_data.get("authors", "")
    year = paper_data.get("year", "")
    citations = paper_data.get("citations", 0) or 0
    paper_type = paper_data.get("paper_type", "primary")
    domain_label = paper_data.get("domain_label", "")

    body = "\n\n# %s\n" % title
    body += "\n**著者**: %s\n" % authors
    body += "**年**: %s | **被引用数**: %s\n" % (year, citations)
    body += "**タイプ**: %s | **分野**: %s\n" % (paper_type, domain_label)

    if abstract:
        body += "\n## Abstract\n\n%s\n" % abstract

    return frontmatter + body


def build_index_entry(paper_data, file_path):
    # type: (Dict, str) -> Dict
    """Build index.jsonl entry from paper data.

    Ensures backward compatibility with pipeline_compile.py which reads:
    type, title, file, authors (or author).
    """
    return {
        "type": paper_data.get("type", "paper"),
        "title": paper_data.get("title", ""),
        "file": file_path,
        "authors": paper_data.get("authors", ""),
        "year": paper_data.get("year", 0),
        "citations": paper_data.get("citations", 0),
        "paper_type": paper_data.get("paper_type", "primary"),
        "domain": paper_data.get("domain", ""),
        "source_api": paper_data.get("source_api", ""),
    }


def _escape_yaml(text):
    # type: (str) -> str
    """Escape characters that break YAML double-quoted strings."""
    return text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
