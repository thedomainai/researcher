"""Domain-aware rate limiter for ethical crawling."""

import asyncio
import time
from collections import defaultdict
from typing import Optional
from urllib.parse import urlparse


class RateLimiter:
    """Enforces per-domain rate limits to avoid overloading servers."""

    def __init__(self, domain_intervals=None, default_interval=1.5):
        # type: (Optional[dict], float) -> None
        self._last_request = defaultdict(float)  # type: dict
        self._domain_intervals = domain_intervals or {}
        self._default_interval = default_interval

    def _get_domain(self, url):
        # type: (str) -> str
        return urlparse(url).netloc

    def _get_interval(self, domain):
        # type: (str) -> float
        return self._domain_intervals.get(domain, self._default_interval)

    async def wait(self, url):
        # type: (str) -> None
        domain = self._get_domain(url)
        interval = self._get_interval(domain)
        elapsed = time.monotonic() - self._last_request[domain]
        if elapsed < interval:
            await asyncio.sleep(interval - elapsed)
        self._last_request[domain] = time.monotonic()

    def wait_sync(self, url):
        # type: (str) -> None
        domain = self._get_domain(url)
        interval = self._get_interval(domain)
        elapsed = time.monotonic() - self._last_request[domain]
        if elapsed < interval:
            time.sleep(interval - elapsed)
        self._last_request[domain] = time.monotonic()
