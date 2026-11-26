# feeds/anthropic_research — Anthropic research posts

Posts from <https://www.anthropic.com/research>, fetched as they appear. Independent of `raw/` and `wiki/`: not part of the daily pipeline or Tier classification.

Anthropic publishes no RSS feed or webhook, so `tools/fetch_anthropic_research.py` polls `sitemap.xml` and fetches every `/research/<slug>` URL that is not yet in the index. The launchd job `com.researcher.anthropic-research` (`config/com.researcher.anthropic-research.plist`) runs it hourly and at login, and shows a macOS notification for new posts.

## Files

- `index.jsonl` — one post per line: `url`, `slug`, `title`, `description`, `published`, `lastmod`, `first_seen`, `body_chars`, `file`
- `posts/<published>-<slug>.md` — frontmatter plus body text. Not tracked by git: the repository is public and the text is third-party content

## Usage

```bash
python3 tools/fetch_anthropic_research.py --dry-run   # list new URLs only
python3 tools/fetch_anthropic_research.py             # fetch new posts
grep -l "interpretability" feeds/anthropic_research/posts/*.md
```

A changed `lastmod` does not trigger a refetch (the site bumps it in bulk). To refetch a post, delete its line in `index.jsonl` and its file, then run the tool.

## launchd

```bash
cp config/com.researcher.anthropic-research.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.researcher.anthropic-research.plist
launchctl kickstart -k gui/$(id -u)/com.researcher.anthropic-research   # run now
launchctl bootout gui/$(id -u)/com.researcher.anthropic-research        # stop
```
