"""OpenAlex API client for paper fetching."""

from datetime import datetime
from typing import Dict, List, Optional

import httpx

from .rate_limiter import RateLimiter
from .utils import (
    detect_paper_type,
    inv_index_to_text,
    normalize_doi,
    normalize_openalex_id,
)


OA_BASE = "https://api.openalex.org"


class OpenAlexClient:
    """Client for OpenAlex API with rate limiting."""

    def __init__(self, rate_limiter, mailto="researcher-bot@example.com"):
        # type: (RateLimiter, str) -> None
        self.rl = rate_limiter
        self.mailto = mailto

    def _request(self, url, params=None):
        # type: (str, Optional[Dict]) -> Optional[Dict]
        """Make a rate-limited GET request."""
        self.rl.wait_sync(url)
        if params is None:
            params = {}
        params["mailto"] = self.mailto
        try:
            r = httpx.get(url, params=params, timeout=30)
            if r.status_code == 200:
                return r.json()
            else:
                print("      OpenAlex %d: %s" % (r.status_code, url[:80]))
                return None
        except Exception as e:
            print("      OpenAlex error: %s" % e)
            return None

    def search(self, query, since=None, per_page=5, sort="relevance_score:desc"):
        # type: (str, Optional[str], int, str) -> List[Dict]
        """Search for papers by keyword."""
        params = {
            "search": query,
            "per_page": per_page,
            "sort": sort,
        }  # type: Dict
        if since:
            params["filter"] = "from_publication_date:%s" % since
        data = self._request(OA_BASE + "/works", params)
        if data:
            return data.get("results", [])
        return []

    def get_work(self, work_id):
        # type: (str) -> Optional[Dict]
        """Get a single work by OpenAlex ID or DOI.

        work_id can be: "W1234567890", "https://openalex.org/W1234567890",
                        "10.1234/xxxxx", "https://doi.org/10.1234/xxxxx"
        """
        # Normalize to URL form for the API
        if work_id.startswith("W"):
            url = "%s/works/%s" % (OA_BASE, work_id)
        elif work_id.startswith("https://openalex.org/"):
            url = "%s/works/%s" % (OA_BASE, work_id.split("/")[-1])
        elif work_id.startswith("https://doi.org/") or work_id.startswith("10."):
            doi = work_id
            if not doi.startswith("https://"):
                doi = "https://doi.org/%s" % doi
            url = "%s/works/%s" % (OA_BASE, doi)
        else:
            url = "%s/works/%s" % (OA_BASE, work_id)
        return self._request(url)

    def get_cited_by(self, work_id, min_citations=0, per_page=25):
        # type: (str, int, int) -> List[Dict]
        """Get papers that cite the given work, sorted by citation count."""
        oa_id = normalize_openalex_id(work_id)
        if not oa_id:
            return []

        params = {
            "filter": "cites:%s" % oa_id,
            "sort": "cited_by_count:desc",
            "per_page": per_page,
        }  # type: Dict
        if min_citations > 0:
            params["filter"] += ",cited_by_count:>%d" % min_citations

        data = self._request(OA_BASE + "/works", params)
        if data:
            return data.get("results", [])
        return []

    def get_references(self, work_id):
        # type: (str) -> List[str]
        """Get referenced work IDs from a work's metadata."""
        work = self.get_work(work_id)
        if not work:
            return []
        refs = work.get("referenced_works", [])
        return [normalize_openalex_id(r) for r in refs if r]

    def extract_paper_data(self, work, domain, domain_label):
        # type: (Dict, str, str) -> Dict
        """Convert OpenAlex Work object to unified paper_data dict."""
        title = (work.get("title") or "untitled").replace("\n", " ")
        abstract = inv_index_to_text(work.get("abstract_inverted_index"))
        year = work.get("publication_year") or 0
        citations = work.get("cited_by_count") or 0
        doi = normalize_doi(work.get("doi", ""))
        oa_id = normalize_openalex_id(work.get("id", ""))

        authorships = work.get("authorships") or []
        authors = ", ".join(
            a.get("author", {}).get("display_name", "")
            for a in authorships[:5]
        )
        if len(authorships) > 5:
            authors += " (+%d)" % (len(authorships) - 5)

        paper_type = detect_paper_type(title, abstract)

        return {
            "title": title,
            "authors": authors,
            "year": year,
            "citations": citations,
            "paper_type": paper_type,
            "domain": domain,
            "domain_label": domain_label,
            "source_api": "openalex",
            "fetched": datetime.now().isoformat(),
            "doi": doi,
            "openalex_id": oa_id,
            "semantic_scholar_id": "",
            "arxiv_id": "",
            "url": work.get("doi") or work.get("id", ""),
            "abstract": abstract,
        }
