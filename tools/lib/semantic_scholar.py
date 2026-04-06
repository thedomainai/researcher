"""Semantic Scholar API client for paper fetching."""

from typing import Dict, List, Optional

import httpx

from .rate_limiter import RateLimiter
from .utils import detect_paper_type, normalize_doi


SS_BASE = "https://api.semanticscholar.org/graph/v1"
SS_FIELDS = (
    "paperId,title,abstract,year,citationCount,influentialCitationCount,"
    "authors,publicationTypes,externalIds,isOpenAccess,openAccessPdf"
)


class SemanticScholarClient:
    """Client for Semantic Scholar Graph API with rate limiting."""

    def __init__(self, rate_limiter, api_key=None):
        # type: (RateLimiter, Optional[str]) -> None
        self.rl = rate_limiter
        self.api_key = api_key

    def _headers(self):
        # type: () -> Dict
        h = {"Accept": "application/json"}
        if self.api_key:
            h["x-api-key"] = self.api_key
        return h

    def _request(self, url, params=None):
        # type: (str, Optional[Dict]) -> Optional[Dict]
        self.rl.wait_sync(url)
        if params is None:
            params = {}
        try:
            r = httpx.get(url, params=params, headers=self._headers(), timeout=30)
            if r.status_code == 200:
                return r.json()
            else:
                print("      S2 %d: %s" % (r.status_code, url[:80]))
                return None
        except Exception as e:
            print("      S2 error: %s" % e)
            return None

    def search(self, query, limit=20, min_citations=50):
        # type: (str, int, int) -> List[Dict]
        """Search papers by free-text query."""
        url = "%s/paper/search" % SS_BASE
        params = {
            "query": query,
            "limit": min(limit, 100),
            "fields": SS_FIELDS,
        }
        data = self._request(url, params)
        if not data or "data" not in data:
            return []
        return [
            self._normalize(p)
            for p in data["data"]
            if p.get("citationCount", 0) >= min_citations
        ]

    def get_paper(self, paper_id):
        # type: (str) -> Optional[Dict]
        """Fetch a single paper by Semantic Scholar ID, DOI, or arXiv ID.

        paper_id examples:
          - "649def34f8be52c8b66281af98ae884c09aef38b"  (S2 hash)
          - "DOI:10.18653/v1/2020.acl-main.463"
          - "ARXIV:2104.09864"
        """
        url = "%s/paper/%s" % (SS_BASE, paper_id)
        data = self._request(url, {"fields": SS_FIELDS})
        if not data:
            return None
        return self._normalize(data)

    def get_citations(self, paper_id, limit=50):
        # type: (str, int) -> List[Dict]
        """Fetch papers that cite the given paper."""
        url = "%s/paper/%s/citations" % (SS_BASE, paper_id)
        params = {"fields": "paperId,title,year,citationCount,externalIds", "limit": min(limit, 500)}
        data = self._request(url, params)
        if not data or "data" not in data:
            return []
        results = []
        for item in data["data"]:
            p = item.get("citingPaper", {})
            if p:
                results.append(self._normalize(p))
        return results

    def get_references(self, paper_id, limit=50):
        # type: (str, int) -> List[Dict]
        """Fetch papers referenced by the given paper."""
        url = "%s/paper/%s/references" % (SS_BASE, paper_id)
        params = {"fields": "paperId,title,year,citationCount,externalIds", "limit": min(limit, 500)}
        data = self._request(url, params)
        if not data or "data" not in data:
            return []
        results = []
        for item in data["data"]:
            p = item.get("citedPaper", {})
            if p:
                results.append(self._normalize(p))
        return results

    def _normalize(self, raw):
        # type: (Dict) -> Dict
        """Normalize a S2 paper dict to the project's internal schema."""
        paper_id = raw.get("paperId", "")
        ext = raw.get("externalIds") or {}
        arxiv_id = ext.get("ArXiv", "")
        doi = normalize_doi(ext.get("DOI", ""))

        title = raw.get("title", "")
        abstract = raw.get("abstract", "") or ""
        year = raw.get("year") or 0
        citations = raw.get("citationCount") or 0
        influential = raw.get("influentialCitationCount") or 0

        authors = [a.get("name", "") for a in (raw.get("authors") or [])]

        pub_types = raw.get("publicationTypes") or []
        paper_type = detect_paper_type(title, abstract)

        oa_pdf = raw.get("openAccessPdf") or {}
        pdf_url = oa_pdf.get("url", "")

        return {
            "source": "semantic_scholar",
            "s2_id": paper_id,
            "arxiv_id": arxiv_id,
            "doi": doi,
            "title": title,
            "abstract": abstract,
            "year": year,
            "citations": citations,
            "influential_citations": influential,
            "authors": authors,
            "paper_type": paper_type,
            "pdf_url": pdf_url,
        }
