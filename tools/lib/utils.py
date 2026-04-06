"""Shared utility functions for paper fetching pipeline."""

import hashlib
import re
from typing import Optional


def slugify(text):
    # type: (str) -> str
    """Convert text to URL-safe slug, max 80 chars."""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[\s]+', '-', text).strip('-')[:80]


def title_hash(title):
    # type: (str) -> str
    """Normalize title and return MD5 hash prefix for deduplication."""
    normalized = re.sub(r'[^a-z0-9]', '', title.lower())
    return hashlib.md5(normalized.encode()).hexdigest()[:16]


def detect_paper_type(title, abstract):
    # type: (str, str) -> str
    """Detect paper type from title and abstract keywords.

    Returns: "meta_analysis" | "systematic_review" | "primary"
    """
    title_lower = (title or "").lower()
    abstract_lower = (abstract or "").lower()

    # Meta-analysis keywords (check first — more specific)
    ma_title_kw = ["meta-analysis", "meta analysis", "quantitative synthesis"]
    ma_abstract_kw = [
        "effect size", "pooled estimate", "heterogeneity",
        "forest plot", "random effects",
    ]
    if any(k in title_lower for k in ma_title_kw):
        return "meta_analysis"
    if sum(1 for k in ma_abstract_kw if k in abstract_lower) >= 2:
        return "meta_analysis"

    # Systematic review keywords
    sr_title_kw = ["systematic review", "scoping review", "literature review", "survey"]
    sr_abstract_kw = [
        "prisma", "systematic search", "inclusion criteria",
        "excluded studies",
    ]
    if any(k in title_lower for k in sr_title_kw):
        return "systematic_review"
    if sum(1 for k in sr_abstract_kw if k in abstract_lower) >= 2:
        return "systematic_review"

    return "primary"


def tier_estimate(citations, influential_citations, paper_type, min_citations):
    # type: (int, int, str, int) -> int
    """Heuristic tier estimation without LLM.

    Tier 1: Invariant principles (SR/MA, or high-citation with influence)
    Tier 2: Vanishing constraint analysis (moderate citations)
    Tier 3: Skip candidate
    """
    citations = citations or 0
    influential_citations = influential_citations or 0

    if paper_type in ("meta_analysis", "systematic_review"):
        return 1
    if citations >= min_citations and influential_citations >= 10:
        return 1
    if citations >= min_citations * 0.5:
        return 2
    return 3


def inv_index_to_text(inv):
    # type: (Optional[dict]) -> str
    """Reconstruct abstract text from OpenAlex inverted index format."""
    if not inv:
        return ""
    word_positions = []
    for word, positions in inv.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)


def normalize_doi(doi):
    # type: (Optional[str]) -> str
    """Normalize DOI to bare format (strip URL prefix)."""
    if not doi:
        return ""
    doi = doi.strip()
    if doi.startswith("https://doi.org/"):
        return doi[len("https://doi.org/"):]
    if doi.startswith("http://doi.org/"):
        return doi[len("http://doi.org/"):]
    return doi


def normalize_openalex_id(oa_id):
    # type: (Optional[str]) -> str
    """Normalize OpenAlex ID to short form (e.g., W1234567890)."""
    if not oa_id:
        return ""
    oa_id = oa_id.strip()
    if oa_id.startswith("https://openalex.org/"):
        return oa_id[len("https://openalex.org/"):]
    return oa_id
