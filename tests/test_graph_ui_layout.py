import subprocess
import tempfile
import time
import unittest
from pathlib import Path
import re
from urllib.parse import quote

from PIL import Image

try:
    from playwright.sync_api import Error as PlaywrightError
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover - environment specific
    PlaywrightError = Exception
    sync_playwright = None


BASE = Path(__file__).resolve().parents[1]
GRAPH_BUILD = BASE / "tools" / "build_graph_ui.py"
READER_BUILD = BASE / "tools" / "build_reader.py"
INDEX_BUILD = BASE / "tools" / "build_index_ui.py"
GRAPH_PAGE = BASE / "wiki" / "graph" / "index.html"
READER_PAGE = BASE / "wiki" / "reader.html"
INDEX_PAGE = BASE / "wiki" / "index.html"
ARTIFACT_DIR = Path(tempfile.gettempdir()) / "researcher-ui-screens"
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

GRAPH_READY_SCRIPT = """
return document.readyState === 'complete'
  && !!document.querySelector('#stage-canvas-shell')
  && document.querySelector('#stage-canvas-shell').clientHeight > 220
  && document.querySelectorAll('.stage-brief-card').length === 2;
"""

READER_READY_SCRIPT = """
return document.readyState === 'complete'
  && !!document.querySelector('.reader-stage-shell')
  && !!document.querySelector('#article-list')
  && !!document.querySelector('#article-body')
  && document.querySelector('#stage-title')?.textContent.length > 0
  && document.querySelectorAll('.queue-card').length >= 1;
"""

INDEX_READY_SCRIPT = """
return document.readyState === 'complete'
  && !!document.querySelector('#catalog-sections')
  && !!document.querySelector('.stage-shell')
  && document.querySelectorAll('.catalog-card').length >= 1;
"""

LAYOUT_SCRIPT = """
function rectFor(selector){
  const el = document.querySelector(selector);
  if (!el) return null;
  const r = el.getBoundingClientRect();
  return {left:r.left, top:r.top, right:r.right, bottom:r.bottom, width:r.width, height:r.height};
}
function rectsFor(selector){
  return Array.from(document.querySelectorAll(selector)).map((el) => {
    const r = el.getBoundingClientRect();
    return {left:r.left, top:r.top, right:r.right, bottom:r.bottom, width:r.width, height:r.height};
  });
}
function gridColumnCount(selector){
  const el = document.querySelector(selector);
  if (!el) return 0;
  const value = getComputedStyle(el).gridTemplateColumns;
  if (!value || value === 'none') return 0;
  return value.trim().split(/\\s+/).length;
}
function directChildColumnCount(selector){
  const el = document.querySelector(selector);
  if (!el) return 0;
  const lefts = new Set(
    Array.from(el.children)
      .map((child) => Math.round(child.getBoundingClientRect().left))
      .filter((left) => Number.isFinite(left))
  );
  return lefts.size;
}
function overflowY(selector){
  const el = document.querySelector(selector);
  return el ? getComputedStyle(el).overflowY : null;
}
return {
  viewportWidth: window.innerWidth,
  viewportHeight: window.innerHeight,
  devicePixelRatio: window.devicePixelRatio || 1,
  documentWidth: document.documentElement.scrollWidth,
  documentHeight: document.documentElement.scrollHeight,
  horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  rail: rectFor('.page-rail'),
  shell: rectFor('.shell, .reader-main'),
  hero: rectFor('.hero'),
  metricGrid: rectFor('.metric-grid'),
  workspace: rectFor('.layout'),
  control: rectFor('.control-panel'),
  analysis: rectFor('.analysis-column'),
  stageShell: rectFor('.stage-shell'),
  stage: rectFor('#stage'),
  stageHeader: rectFor('.stage-header'),
  stageMeta: rectFor('.stage-meta-row'),
  chrome: rectFor('.stage-chrome'),
  canvasShell: rectFor('#stage-canvas-shell'),
  canvas: rectFor('canvas#graph'),
  briefs: rectFor('.stage-briefs'),
  inspector: rectFor('.inspector-panel'),
  dock: rectFor('.dock'),
  inspectorGrid: rectFor('.inspector-grid'),
  list: rectFor('#list, .control-panel'),
  briefCards: rectsFor('.stage-brief-card'),
  navCards: rectsFor('.page-nav > *'),
  metricCards: rectsFor('.metric-grid > *'),
  heroCards: rectsFor('.hero > *'),
  workspaceCards: rectsFor('.layout > *'),
  dockCards: rectsFor('.dock > *'),
  inspectorCards: rectsFor('.inspector-grid > *'),
  legendItems: rectsFor('.legend-item'),
  toolbarChips: rectsFor('.stage-toolbar .stage-chip'),
  chromeChips: rectsFor('.stage-chrome-right .stage-chip'),
  pillRects: rectsFor('.pill-row .pill'),
  metricStripCards: rectsFor('.metric-strip > *'),
  layoutColumns: directChildColumnCount('.layout'),
  navColumns: gridColumnCount('.page-nav'),
  metricColumns: gridColumnCount('.metric-grid'),
  controlOverflowY: overflowY('.control-panel'),
  inspectorOverflowY: overflowY('.inspector-panel'),
  canvasBitmapWidth: document.querySelector('canvas#graph')?.width || 0,
  canvasBitmapHeight: document.querySelector('canvas#graph')?.height || 0,
  legacyStageInfoCount: document.querySelectorAll('.stage-info-card').length,
  legacyDossierCount: document.querySelectorAll('.dossier').length,
  containsLegacyStageText: document.body.innerText.includes('Why this view exists') || document.body.innerText.includes('Interaction model'),
  hasBrand: !!document.querySelector('.page-brand'),
  railText: (document.querySelector('.page-rail')?.innerText || '').trim()
};
"""

READER_LAYOUT_SCRIPT = """
function rectFor(selector){
  const el = document.querySelector(selector);
  if (!el) return null;
  const r = el.getBoundingClientRect();
  return {left:r.left, top:r.top, right:r.right, bottom:r.bottom, width:r.width, height:r.height};
}
function rectsFor(selector){
  return Array.from(document.querySelectorAll(selector)).map((el) => {
    const r = el.getBoundingClientRect();
    return {left:r.left, top:r.top, right:r.right, bottom:r.bottom, width:r.width, height:r.height};
  });
}
function gridColumnCount(selector){
  const el = document.querySelector(selector);
  if (!el) return 0;
  const value = getComputedStyle(el).gridTemplateColumns;
  if (!value || value === 'none') return 0;
  return value.trim().split(/\\s+/).length;
}
function directChildColumnCount(selector){
  const el = document.querySelector(selector);
  if (!el) return 0;
  const lefts = new Set(
    Array.from(el.children)
      .map((child) => Math.round(child.getBoundingClientRect().left))
      .filter((left) => Number.isFinite(left))
  );
  return lefts.size;
}
return {
  viewportWidth: window.innerWidth,
  viewportHeight: window.innerHeight,
  documentWidth: document.documentElement.scrollWidth,
  documentHeight: document.documentElement.scrollHeight,
  horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  rail: rectFor('.page-rail'),
  shell: rectFor('.shell, .reader-main'),
  hero: rectFor('.hero'),
  metricGrid: rectFor('.metric-grid'),
  workspace: rectFor('.layout'),
  queue: rectFor('.reader-queue-panel'),
  analysis: rectFor('.analysis-column'),
  stageShell: rectFor('.reader-stage-shell'),
  readerStage: rectFor('.reader-stage'),
  stageHeader: rectFor('.stage-header'),
  chrome: rectFor('.stage-chrome'),
  bodyCard: rectFor('.article-body-card'),
  body: rectFor('#article-body'),
  briefs: rectFor('.stage-briefs'),
  companion: rectFor('#reader-companion'),
  companionGrid: rectFor('.companion-grid'),
  queueList: rectFor('#article-list'),
  heroCards: rectsFor('.hero > *'),
  metricCards: rectsFor('.metric-grid > *'),
  queueCards: rectsFor('.queue-card'),
  queueMeta: rectsFor('.queue-meta > *'),
  stageToolbar: rectsFor('.stage-toolbar > *'),
  chromeChips: rectsFor('.stage-chrome-right > *'),
  articleMetrics: rectsFor('.article-metric-strip > *'),
  briefCards: rectsFor('.stage-brief-card'),
  companionCards: rectsFor('.companion-grid > *'),
  companionActions: rectsFor('.companion-actions > *'),
  tierChips: rectsFor('#tier-chips > *'),
  pills: rectsFor('.pill-row > *'),
  layoutColumns: directChildColumnCount('.layout'),
  navColumns: gridColumnCount('.page-nav'),
  metricColumns: gridColumnCount('.metric-grid'),
  queueCardCount: document.querySelectorAll('.queue-card').length,
  hasBrand: !!document.querySelector('.page-brand'),
  railText: (document.querySelector('.page-rail')?.innerText || '').trim(),
  bodyTextLength: (document.querySelector('#article-body')?.innerText || '').trim().length,
  bodyTableCount: document.querySelectorAll('#article-body table').length,
  bodyHasEmpty: !!document.querySelector('#article-body .empty'),
  companionHasEmpty: !!document.querySelector('#reader-companion .empty'),
  stageTitle: document.querySelector('#stage-title')?.textContent || ''
};
"""

INDEX_LAYOUT_SCRIPT = """
function rectFor(selector){
  const el = document.querySelector(selector);
  if (!el) return null;
  const r = el.getBoundingClientRect();
  return {left:r.left, top:r.top, right:r.right, bottom:r.bottom, width:r.width, height:r.height};
}
function rectsFor(selector){
  return Array.from(document.querySelectorAll(selector)).map((el) => {
    const r = el.getBoundingClientRect();
    return {left:r.left, top:r.top, right:r.right, bottom:r.bottom, width:r.width, height:r.height};
  });
}
function gridColumnCount(selector){
  const el = document.querySelector(selector);
  if (!el) return 0;
  const value = getComputedStyle(el).gridTemplateColumns;
  if (!value || value === 'none') return 0;
  return value.trim().split(/\\s+/).length;
}
function directChildColumnCount(selector){
  const el = document.querySelector(selector);
  if (!el) return 0;
  const lefts = new Set(
    Array.from(el.children)
      .map((child) => Math.round(child.getBoundingClientRect().left))
      .filter((left) => Number.isFinite(left))
  );
  return lefts.size;
}
return {
  viewportWidth: window.innerWidth,
  viewportHeight: window.innerHeight,
  documentWidth: document.documentElement.scrollWidth,
  documentHeight: document.documentElement.scrollHeight,
  horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  rail: rectFor('.page-rail'),
  shell: rectFor('.shell'),
  hero: rectFor('.hero'),
  metricGrid: rectFor('.metric-grid'),
  workspace: rectFor('.layout'),
  control: rectFor('.control-panel'),
  analysis: rectFor('.analysis-column'),
  stageShell: rectFor('.stage-shell'),
  stage: rectFor('#stage'),
  stageHeader: rectFor('.stage-header'),
  chrome: rectFor('.stage-chrome'),
  catalogBody: rectFor('.catalog-stage-body'),
  sections: rectFor('#catalog-sections'),
  briefs: rectFor('.stage-briefs'),
  summaryStrip: rectFor('.catalog-summary-strip'),
  heroCards: rectsFor('.hero > *'),
  metricCards: rectsFor('.metric-grid > *'),
  navCards: rectsFor('.page-nav > *'),
  summaryCards: rectsFor('.catalog-summary-strip > *'),
  sectionCards: rectsFor('.catalog-section'),
  catalogCards: rectsFor('.catalog-card'),
  briefCards: rectsFor('.stage-brief-card'),
  tierChips: rectsFor('#tier-chips > *'),
  layoutColumns: directChildColumnCount('.layout'),
  navColumns: gridColumnCount('.page-nav'),
  metricColumns: gridColumnCount('.metric-grid'),
  sectionCount: document.querySelectorAll('.catalog-section').length,
  cardCount: document.querySelectorAll('.catalog-card').length,
  hasBrand: !!document.querySelector('.page-brand'),
  railText: (document.querySelector('.page-rail')?.innerText || '').trim()
};
"""

GRAPH_VISUAL_PROBE_SCRIPT = """
const canvas = document.querySelector('canvas#graph');
const node = resolvedNodes.slice().sort((a, b) => radiusFor(b) - radiusFor(a))[0];
state.selected = node.id;
state.focusMode = false;
centerOnNode(node);
update();
const rect = canvas.getBoundingClientRect();
const p = worldToScreen(node.x, node.y);
const r = radiusFor(node) * state.scale;
const abs = (x, y) => ({x: rect.left + window.scrollX + x, y: rect.top + window.scrollY + y});
const bodyStyle = getComputedStyle(document.body);
return {
  bodyColor: bodyStyle.color,
  nodeId: node.id,
  nodeRadius: r,
  canvasBackground: abs(rect.width * 0.05, rect.height * 0.05),
  nodeCenter: abs(p.x, p.y),
  nodeUpperLeft: abs(p.x - r * 0.28, p.y - r * 0.28),
  nodeLowerRight: abs(p.x + r * 0.32, p.y + r * 0.32),
};
"""

CSS_RGB_RE = re.compile(r"rgba?\((\d+),\s*(\d+),\s*(\d+)")


def _rgb_from_css(value):
    match = CSS_RGB_RE.search(value or "")
    if not match:
        raise AssertionError(f"could not parse css color: {value!r}")
    return tuple(int(v) for v in match.groups())


def _luma(rgb):
    r, g, b = rgb[:3]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _rgb_delta(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3))


def _pixel(path: Path, point):
    with Image.open(path).convert("RGBA") as image:
        return image.getpixel((round(point["x"]), round(point["y"])))


def _artifact_path(ref) -> Path:
    path = Path(ref)
    if path.exists():
        return path
    candidate = ARTIFACT_DIR / f"{ref}.png"
    return candidate


class PlaywrightSession:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def __enter__(self):
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=True)
            self.page = self.browser.new_page(device_scale_factor=1)
            return self
        except Exception:
            self.__exit__(None, None, None)
            raise

    def __exit__(self, exc_type, exc, tb):
        if self.page:
            self.page.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def set_window(self, width: int, height: int):
        self.page.set_viewport_size({"width": width, "height": height})

    def navigate(self, url: str):
        self.page.goto(url, wait_until="load")

    def execute(self, script: str, args=None):
        wrapped = f"(...args) => {{ {script} }}"
        return self.page.evaluate(wrapped, args or [])

    def screenshot(self, output_path: Path):
        self.page.screenshot(path=str(output_path), full_page=True)


def rects_overlap(a, b) -> bool:
    return a["left"] < b["right"] and a["right"] > b["left"] and a["top"] < b["bottom"] and a["bottom"] > b["top"]


@unittest.skipUnless(sync_playwright is not None, "playwright is required for screenshot layout tests")
class GraphUiLayoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(["python3", str(GRAPH_BUILD)], check=True, cwd=BASE)
        subprocess.run(["python3", str(READER_BUILD)], check=True, cwd=BASE)
        subprocess.run(["python3", str(INDEX_BUILD)], check=True, cwd=BASE)

    def _capture_page(self, page_path: Path, width: int, height: int, label: str, readiness_script: str, layout_script: str = LAYOUT_SCRIPT):
        with PlaywrightSession() as session:
            session.set_window(width, height)
            session.navigate(page_path.resolve().as_uri())
            self._wait_for_render(session, readiness_script)
            screenshot_path = ARTIFACT_DIR / f"{label}.png"
            session.screenshot(screenshot_path)
            with Image.open(screenshot_path) as image:
                image_size = image.size
            layout = session.execute(layout_script)
            layout["imageWidth"], layout["imageHeight"] = image_size
            return layout, screenshot_path

    def _wait_for_render(self, session: PlaywrightSession, readiness_script: str, timeout: float = 15.0):
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                if session.execute(readiness_script):
                    time.sleep(0.35)
                    return
            except PlaywrightError:
                pass
            time.sleep(0.1)
        raise TimeoutError("graph UI did not finish rendering")

    def _save_interaction_screenshot(self, session: PlaywrightSession, label: str):
        session.screenshot(ARTIFACT_DIR / f"{label}.png")

    def assert_rect_present(self, rect, message: str):
        self.assertIsNotNone(rect, message)
        self.assertGreater(rect["width"], 0, message)
        self.assertGreater(rect["height"], 0, message)

    def assert_rect_separation(self, left_rect, right_rect, message: str):
        self.assert_rect_present(left_rect, message)
        self.assert_rect_present(right_rect, message)
        self.assertLessEqual(left_rect["right"], right_rect["left"] + 2, message)

    def assert_vertical_flow(self, upper_rect, lower_rect, message: str):
        self.assert_rect_present(upper_rect, message)
        self.assert_rect_present(lower_rect, message)
        self.assertGreaterEqual(lower_rect["top"], upper_rect["bottom"] - 1, message)

    def assert_rect_within_viewport(self, rect, layout, message: str):
        self.assert_rect_present(rect, message)
        self.assertGreaterEqual(rect["left"], -1, message)
        self.assertLessEqual(rect["right"], layout["viewportWidth"] + 1, message)

    def assert_rect_within_parent(self, child_rect, parent_rect, message: str):
        self.assert_rect_present(child_rect, message)
        self.assert_rect_present(parent_rect, message)
        self.assertGreaterEqual(child_rect["left"], parent_rect["left"] - 1, message)
        self.assertLessEqual(child_rect["right"], parent_rect["right"] + 1, message)
        self.assertGreaterEqual(child_rect["top"], parent_rect["top"] - 1, message)
        self.assertLessEqual(child_rect["bottom"], parent_rect["bottom"] + 1, message)

    def assert_no_horizontal_overflow(self, layout, screenshot_path):
        self.assertFalse(layout["horizontalOverflow"], f"horizontal overflow detected; screenshot={screenshot_path}")
        self.assertLessEqual(layout["documentWidth"], layout["viewportWidth"] + 1, f"document width exceeds viewport; screenshot={screenshot_path}")

    def assert_dark_shell(self, screenshot_path):
        pixel = _pixel(_artifact_path(screenshot_path), {"x": 8, "y": 8})
        self.assertLess(_luma(pixel), 75, f"page shell should remain dark; screenshot={screenshot_path}")

    def assert_no_pair_overlap(self, rects, screenshot_path, label):
        for i, first in enumerate(rects):
            for j, second in enumerate(rects):
                if i >= j:
                    continue
                self.assertFalse(rects_overlap(first, second), f"{label} items {i} and {j} overlap; screenshot={screenshot_path}")

    def assert_rect_group_within_viewport(self, rects, layout, screenshot_path, label):
        for index, rect in enumerate(rects):
            self.assert_rect_within_viewport(rect, layout, f"{label} item {index} escaped viewport; screenshot={screenshot_path}")

    def assert_canvas_matches_shell(self, layout, screenshot_path):
        self.assert_rect_present(layout["canvasShell"], f"canvas shell missing; screenshot={screenshot_path}")
        self.assert_rect_present(layout["canvas"], f"canvas missing; screenshot={screenshot_path}")
        self.assertLessEqual(abs(layout["canvasShell"]["width"] - layout["canvas"]["width"]), 2.5, f"canvas width mismatches shell; screenshot={screenshot_path}")
        self.assertLessEqual(abs(layout["canvasShell"]["height"] - layout["canvas"]["height"]), 2.5, f"canvas height mismatches shell; screenshot={screenshot_path}")
        self.assertGreaterEqual(layout["canvasBitmapWidth"], int(layout["canvasShell"]["width"] * layout["devicePixelRatio"]) - 2, f"canvas bitmap width does not track DPR; screenshot={screenshot_path}")
        self.assertGreaterEqual(layout["canvasBitmapHeight"], int(layout["canvasShell"]["height"] * layout["devicePixelRatio"]) - 2, f"canvas bitmap height does not track DPR; screenshot={screenshot_path}")

    def assert_common_graph_invariants(self, layout, screenshot_path):
        self.assert_no_horizontal_overflow(layout, screenshot_path)
        self.assert_dark_shell(screenshot_path)
        self.assertFalse(layout["hasBrand"], f"sidebar should not contain a product brand block; screenshot={screenshot_path}")
        self.assertNotIn("Current view", layout["railText"], f"sidebar should not repeat current-view label; screenshot={screenshot_path}")
        self.assertNotIn("Knowledge Workspace", layout["railText"], f"sidebar should not repeat product title; screenshot={screenshot_path}")
        self.assertEqual(layout["legacyStageInfoCount"], 0, f"legacy stage-info cards should not remain; screenshot={screenshot_path}")
        self.assertEqual(layout["legacyDossierCount"], 0, f"legacy dossier class should not remain; screenshot={screenshot_path}")
        self.assertFalse(layout["containsLegacyStageText"], f"legacy explanatory stage copy returned; screenshot={screenshot_path}")

        for key in ["hero", "metricGrid", "workspace", "control", "analysis", "stageShell", "stage", "stageHeader", "stageMeta", "chrome", "canvasShell", "briefs", "inspector", "dock", "inspectorGrid"]:
            self.assert_rect_present(layout[key], f"{key} missing; screenshot={screenshot_path}")
            self.assert_rect_within_viewport(layout[key], layout, f"{key} escaped viewport width; screenshot={screenshot_path}")

        self.assert_rect_within_parent(layout["analysis"], layout["workspace"], f"analysis column escaped workspace; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["stageShell"], layout["analysis"], f"stage shell escaped analysis column; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["inspector"], layout["analysis"], f"inspector escaped analysis column; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["canvas"], layout["canvasShell"], f"canvas escaped shell; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["chrome"], layout["canvasShell"], f"chrome overlaps canvas; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["canvasShell"], layout["briefs"], f"briefs overlap canvas; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["stageShell"], layout["inspector"], f"inspector should sit below stage; screenshot={screenshot_path}")

        for label, rects in [
            ("stage brief", layout["briefCards"]),
            ("hero", layout["heroCards"]),
            ("metric", layout["metricCards"]),
            ("workspace", layout["workspaceCards"]),
            ("nav", layout["navCards"]),
            ("dock", layout["dockCards"]),
            ("inspector", layout["inspectorCards"]),
            ("legend", layout["legendItems"]),
            ("stage-toolbar", layout["toolbarChips"]),
            ("stage-chrome", layout["chromeChips"]),
            ("pill", layout["pillRects"]),
            ("metric-strip", layout["metricStripCards"]),
        ]:
            self.assert_no_pair_overlap(rects, screenshot_path, label)
            self.assert_rect_group_within_viewport(rects, layout, screenshot_path, label)

        self.assertEqual(len(layout["briefCards"]), 2, f"unexpected stage brief count; screenshot={screenshot_path}")
        self.assert_canvas_matches_shell(layout, screenshot_path)
        max_briefs_ratio = 0.35 if layout["viewportWidth"] > 900 else (0.7 if layout["viewportWidth"] >= 640 else 0.85)
        self.assertLess(layout["briefs"]["height"], layout["canvasShell"]["height"] * max_briefs_ratio, f"briefs should stay subordinate to canvas; screenshot={screenshot_path}")
        if layout["layoutColumns"] > 1:
            self.assertGreater(layout["stageShell"]["width"], layout["control"]["width"], f"stage should stay wider than control panel; screenshot={screenshot_path}")
        self.assertGreaterEqual(layout["canvasShell"]["height"], 320 if layout["viewportWidth"] <= 900 else 440, f"canvas height regressed; screenshot={screenshot_path}")

    def assert_common_reader_invariants(self, layout, screenshot_path):
        self.assert_no_horizontal_overflow(layout, screenshot_path)
        self.assert_dark_shell(screenshot_path)
        self.assertFalse(layout["hasBrand"], f"sidebar should not contain a product brand block; screenshot={screenshot_path}")
        self.assertNotIn("Current view", layout["railText"], f"sidebar should not repeat current-view label; screenshot={screenshot_path}")
        self.assertNotIn("Knowledge Workspace", layout["railText"], f"sidebar should not repeat product title; screenshot={screenshot_path}")

        for key in ["hero", "metricGrid", "workspace", "queue", "analysis", "stageShell", "readerStage", "stageHeader", "chrome", "bodyCard", "body", "briefs", "companion", "queueList"]:
            self.assert_rect_present(layout[key], f"{key} missing; screenshot={screenshot_path}")
            self.assert_rect_within_viewport(layout[key], layout, f"{key} escaped viewport width; screenshot={screenshot_path}")

        self.assert_rect_within_parent(layout["analysis"], layout["workspace"], f"analysis column escaped workspace; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["stageShell"], layout["analysis"], f"reader stage shell escaped analysis column; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["companion"], layout["analysis"], f"reader companion escaped analysis column; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["body"], layout["bodyCard"], f"article body escaped body card; screenshot={screenshot_path}")

        self.assert_vertical_flow(layout["stageHeader"], layout["readerStage"], f"stage header overlaps reader stage; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["chrome"], layout["bodyCard"], f"chrome overlaps article body card; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["bodyCard"], layout["briefs"], f"briefs overlap article body; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["stageShell"], layout["companion"], f"companion should sit below stage; screenshot={screenshot_path}")

        for label, rects in [
            ("reader-hero", layout["heroCards"]),
            ("reader-metric", layout["metricCards"]),
            ("queue-meta", layout["queueMeta"]),
            ("stage-toolbar", layout["stageToolbar"]),
            ("stage-chrome", layout["chromeChips"]),
            ("article-metric", layout["articleMetrics"]),
            ("reader-brief", layout["briefCards"]),
            ("companion", layout["companionCards"]),
            ("companion-actions", layout["companionActions"]),
            ("tier-chip", layout["tierChips"]),
            ("reader-pill", layout["pills"]),
        ]:
            self.assert_no_pair_overlap(rects, screenshot_path, label)
            self.assert_rect_group_within_viewport(rects, layout, screenshot_path, label)

        self.assertEqual(len(layout["briefCards"]), 2, f"reader should keep 2 stage briefs; screenshot={screenshot_path}")
        self.assertGreater(layout["queueCardCount"], 0, f"reader queue unexpectedly empty; screenshot={screenshot_path}")
        self.assertGreater(len(layout["stageTitle"].strip()), 0, f"reader stage title missing; screenshot={screenshot_path}")
        self.assertGreater(layout["bodyTextLength"], 80, f"article body collapsed; screenshot={screenshot_path}")

    def assert_common_index_invariants(self, layout, screenshot_path):
        self.assert_no_horizontal_overflow(layout, screenshot_path)
        self.assert_dark_shell(screenshot_path)
        self.assertFalse(layout["hasBrand"], f"sidebar should not contain a product brand block; screenshot={screenshot_path}")
        self.assertNotIn("Current view", layout["railText"], f"sidebar should not repeat current-view label; screenshot={screenshot_path}")
        self.assertNotIn("Knowledge Workspace", layout["railText"], f"sidebar should not repeat product title; screenshot={screenshot_path}")

        for key in ["hero", "metricGrid", "workspace", "control", "analysis", "stageShell", "stage", "stageHeader", "chrome", "catalogBody", "sections", "briefs", "summaryStrip"]:
            self.assert_rect_present(layout[key], f"{key} missing; screenshot={screenshot_path}")
            self.assert_rect_within_viewport(layout[key], layout, f"{key} escaped viewport width; screenshot={screenshot_path}")

        self.assert_rect_within_parent(layout["analysis"], layout["workspace"], f"index analysis escaped workspace; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["stageShell"], layout["analysis"], f"index stage shell escaped analysis column; screenshot={screenshot_path}")
        self.assert_rect_within_parent(layout["stage"], layout["stageShell"], f"index stage escaped stage shell; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["stageHeader"], layout["stage"], f"stage header overlaps catalog stage; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["chrome"], layout["catalogBody"], f"chrome overlaps catalog body; screenshot={screenshot_path}")
        self.assert_vertical_flow(layout["catalogBody"], layout["briefs"], f"briefs overlap catalog body; screenshot={screenshot_path}")

        for label, rects in [
            ("index-hero", layout["heroCards"]),
            ("index-metric", layout["metricCards"]),
            ("index-nav", layout["navCards"]),
            ("index-summary", layout["summaryCards"]),
            ("index-section", layout["sectionCards"]),
            ("index-card", layout["catalogCards"]),
            ("index-brief", layout["briefCards"]),
            ("index-tier-chip", layout["tierChips"]),
        ]:
            self.assert_no_pair_overlap(rects, screenshot_path, label)
            self.assert_rect_group_within_viewport(rects, layout, screenshot_path, label)

        self.assertGreater(layout["sectionCount"], 0, f"index should render at least one section; screenshot={screenshot_path}")
        self.assertGreater(layout["cardCount"], 0, f"index should render at least one card; screenshot={screenshot_path}")

    def test_graph_layout_desktop_stage_first_dashboard(self):
        layout, screenshot_path = self._capture_page(GRAPH_PAGE, 1440, 1400, "graph-desktop", GRAPH_READY_SCRIPT)
        self.assert_common_graph_invariants(layout, screenshot_path)
        self.assertEqual(layout["layoutColumns"], 2, f"desktop atlas should use 2 columns; screenshot={screenshot_path}")
        self.assertEqual(layout["navColumns"], 0, f"desktop nav should stay in flex mode above 900px; screenshot={screenshot_path}")
        self.assertEqual(layout["metricColumns"], 2, f"desktop metric grid should have 2 columns; screenshot={screenshot_path}")
        self.assert_rect_separation(layout["rail"], layout["shell"], f"sidebar overlaps atlas shell; screenshot={screenshot_path}")
        self.assert_rect_separation(layout["control"], layout["analysis"], f"control panel overlaps analysis column; screenshot={screenshot_path}")
        self.assertIn(layout["controlOverflowY"], ["auto", "scroll"], f"control panel should scroll internally on desktop; screenshot={screenshot_path}")
        self.assertIn(layout["inspectorOverflowY"], ["visible"], f"desktop inspector should render as a normal dashboard panel; screenshot={screenshot_path}")
        self.assertLess(layout["imageHeight"], layout["viewportHeight"] * 2.4, f"desktop screenshot is too tall for a dashboard; screenshot={screenshot_path}")

    def test_graph_layout_breakpoint_matrix(self):
        cases = [
            (1321, 1400, 2, 0, 2),
            (1121, 1500, 2, 0, 2),
            (1120, 1600, 2, 0, 2),
            (901, 1800, 2, 0, 2),
            (900, 2000, 1, 3, 2),
            (641, 2200, 1, 3, 2),
            (640, 2300, 1, 3, 1),
            (390, 2600, 1, 3, 1),
        ]
        for width, height, expected_layout_columns, expected_nav_columns, expected_metric_columns in cases:
            with self.subTest(width=width, height=height):
                layout, screenshot_path = self._capture_page(
                    GRAPH_PAGE,
                    width,
                    height,
                    f"graph-{width}x{height}",
                    GRAPH_READY_SCRIPT,
                )
                self.assert_common_graph_invariants(layout, screenshot_path)
                self.assertEqual(layout["layoutColumns"], expected_layout_columns, f"unexpected workspace column count; screenshot={screenshot_path}")
                self.assertEqual(layout["navColumns"], expected_nav_columns, f"unexpected nav column count; screenshot={screenshot_path}")
                self.assertEqual(layout["metricColumns"], expected_metric_columns, f"unexpected metric column count; screenshot={screenshot_path}")
                if width > 1120:
                    self.assert_rect_separation(layout["rail"], layout["shell"], f"sidebar overlaps shell above 1120px; screenshot={screenshot_path}")
                else:
                    self.assert_vertical_flow(layout["rail"], layout["shell"], f"sidebar should stack above shell at or below 1120px; screenshot={screenshot_path}")
                if expected_layout_columns == 2:
                    self.assert_rect_separation(layout["control"], layout["analysis"], f"control overlaps analysis column; screenshot={screenshot_path}")
                else:
                    self.assert_vertical_flow(layout["control"], layout["analysis"], f"control should stack above analysis column; screenshot={screenshot_path}")

    def test_graph_layout_survives_filters_canvas_and_resize(self):
        with PlaywrightSession() as session:
            session.set_window(1440, 1400)
            session.navigate(GRAPH_PAGE.resolve().as_uri())
            self._wait_for_render(session, GRAPH_READY_SCRIPT)

            session.execute("document.getElementById('focus-hubs').click();")
            self._wait_for_render(session, "return document.querySelector('#overlay-stats')?.textContent.includes('nodes');")
            self._save_interaction_screenshot(session, "graph-focus-hubs")
            self.assert_common_graph_invariants(session.execute(LAYOUT_SCRIPT), "graph-focus-hubs")

            session.execute("document.getElementById('focus-islands').click();")
            self._wait_for_render(session, "return document.querySelector('#chrome-selection')?.textContent.length > 0;")
            self._save_interaction_screenshot(session, "graph-focus-islands")
            self.assert_common_graph_invariants(session.execute(LAYOUT_SCRIPT), "graph-focus-islands")

            session.execute(
                """
                const search = document.getElementById('search');
                search.value = 'ai';
                search.dispatchEvent(new Event('input', {bubbles:true}));
                document.querySelector('[data-tier="1"]').click();
                const slider = document.getElementById('degree-filter');
                slider.value = '3';
                slider.dispatchEvent(new Event('input', {bubbles:true}));
                document.getElementById('focus-gaps').click();
                const domain = document.getElementById('domain-filter');
                if (domain && domain.options.length > 1){
                  domain.value = domain.options[1].value;
                  domain.dispatchEvent(new Event('change', {bubbles:true}));
                }
                """
            )
            self._wait_for_render(session, "return document.querySelector('#overlay-title')?.textContent.length > 0;")
            self._save_interaction_screenshot(session, "graph-focus-gaps")
            self.assert_common_graph_invariants(session.execute(LAYOUT_SCRIPT), "graph-focus-gaps")

            session.execute(
                """
                document.getElementById('show-isolated').click();
                document.getElementById('show-unresolved').click();
                document.getElementById('focus-mode').click();
                document.querySelector('#hub-list [data-slug]')?.click();
                """
            )
            self._wait_for_render(session, "return document.querySelector('#inspector h2')?.textContent.length > 0;")
            self._save_interaction_screenshot(session, "graph-toggle-hub")
            self.assert_common_graph_invariants(session.execute(LAYOUT_SCRIPT), "graph-toggle-hub")

            session.execute("document.querySelector('#gap-list [data-gap-index]')?.click();")
            self._wait_for_render(session, "return document.querySelector('#chrome-selection')?.textContent.length > 0;")
            canvas_center = session.execute(
                """
                const r = document.querySelector('#stage-canvas-shell').getBoundingClientRect();
                return {x: r.left + r.width / 2, y: r.top + r.height / 2};
                """
            )
            session.page.mouse.move(canvas_center["x"], canvas_center["y"])
            session.page.mouse.wheel(0, -360)
            session.page.mouse.down()
            session.page.mouse.move(canvas_center["x"] + 60, canvas_center["y"] + 40)
            session.page.mouse.up()
            self._save_interaction_screenshot(session, "graph-canvas-interaction")
            self.assert_common_graph_invariants(session.execute(LAYOUT_SCRIPT), "graph-canvas-interaction")

            session.set_window(980, 1700)
            self._wait_for_render(session, "return document.querySelector('#stage-canvas-shell')?.clientHeight > 240;")
            self._save_interaction_screenshot(session, "graph-resize-980")
            layout = session.execute(LAYOUT_SCRIPT)
            self.assert_common_graph_invariants(layout, "graph-resize-980")
            self.assertEqual(layout["layoutColumns"], 2, "midwidth resize should keep 2-column graph workspace")

            session.set_window(390, 2600)
            self._wait_for_render(session, "return document.querySelector('#stage-canvas-shell')?.clientHeight > 220;")
            self._save_interaction_screenshot(session, "graph-resize-390")
            layout = session.execute(LAYOUT_SCRIPT)
            self.assert_common_graph_invariants(layout, "graph-resize-390")
            self.assertEqual(layout["layoutColumns"], 1, "mobile resize should stack graph workspace")

            session.set_window(1440, 1400)
            self._wait_for_render(session, "return document.querySelector('#stage-canvas-shell')?.clientHeight > 300;")
            session.execute("document.getElementById('center-selected')?.click(); document.getElementById('toggle-focus')?.click();")
            self._save_interaction_screenshot(session, "graph-resize-return")
            layout = session.execute(LAYOUT_SCRIPT)
            self.assert_common_graph_invariants(layout, "graph-resize-return")
            self.assertEqual(layout["layoutColumns"], 2, "returning to desktop should restore 2-column workspace")

    def test_graph_layout_hash_deeplink_for_long_node(self):
        with PlaywrightSession() as session:
            session.set_window(1440, 1400)
            session.navigate(GRAPH_PAGE.resolve().as_uri())
            self._wait_for_render(session, GRAPH_READY_SCRIPT)
            stress_slug = session.execute(
                """
                return GRAPH.nodes
                  .filter((node) => node.resolved)
                  .sort((a, b) => {
                    const labelDiff = (b.label || '').length - (a.label || '').length;
                    if (labelDiff !== 0) return labelDiff;
                    return (b.description || '').length - (a.description || '').length;
                  })[0].id;
                """
            )
            session.navigate(f"{GRAPH_PAGE.resolve().as_uri()}#node={quote(stress_slug)}")
            self._wait_for_render(session, "return document.querySelector('#inspector h2')?.textContent.length > 0;")
            self._save_interaction_screenshot(session, "graph-hash-stress")
            layout = session.execute(LAYOUT_SCRIPT)
            self.assert_common_graph_invariants(layout, "graph-hash-stress")
            self.assertIn("Selection:", session.execute("return document.querySelector('#chrome-selection')?.textContent || '';"))

    def test_graph_visual_dark_theme_and_node_gradient(self):
        with PlaywrightSession() as session:
            session.set_window(1440, 1400)
            session.navigate(GRAPH_PAGE.resolve().as_uri())
            self._wait_for_render(session, GRAPH_READY_SCRIPT)
            probe = session.execute(GRAPH_VISUAL_PROBE_SCRIPT)
            screenshot_path = ARTIFACT_DIR / "graph-dark-gradient.png"
            session.screenshot(screenshot_path)

        self.assertLess(_luma(_pixel(screenshot_path, {"x": 8, "y": 8})), 75, "graph shell should stay dark")
        self.assertLess(_luma(_pixel(screenshot_path, probe["canvasBackground"])), 95, "graph canvas background should stay dark")
        self.assertGreater(_luma(_rgb_from_css(probe["bodyColor"])), 190, "graph foreground text should stay bright enough")

        center = _pixel(screenshot_path, probe["nodeCenter"])
        upper_left = _pixel(screenshot_path, probe["nodeUpperLeft"])
        lower_right = _pixel(screenshot_path, probe["nodeLowerRight"])
        gradient_delta = max(
            _rgb_delta(center, upper_left),
            _rgb_delta(center, lower_right),
            _rgb_delta(upper_left, lower_right),
        )

        self.assertGreaterEqual(probe["nodeRadius"], 8, "gradient probe should target a meaningful node size")
        self.assertGreaterEqual(gradient_delta, 6, "node fill should no longer be perfectly flat")
        self.assertLessEqual(gradient_delta, 90, "node gradient should remain subtle")

    def test_reader_layout_desktop_queue_stage_companion(self):
        layout, screenshot_path = self._capture_page(
            READER_PAGE,
            1440,
            1600,
            "reader-desktop",
            READER_READY_SCRIPT,
            READER_LAYOUT_SCRIPT,
        )
        self.assert_common_reader_invariants(layout, screenshot_path)
        self.assertEqual(layout["layoutColumns"], 2, f"reader should use 2-column workspace on desktop; screenshot={screenshot_path}")
        self.assertEqual(layout["navColumns"], 0, f"desktop nav should stay in flex mode above 900px; screenshot={screenshot_path}")
        self.assertEqual(layout["metricColumns"], 2, f"desktop metrics should use 2 columns; screenshot={screenshot_path}")
        self.assert_rect_separation(layout["rail"], layout["shell"], f"sidebar overlaps reader shell; screenshot={screenshot_path}")
        self.assert_rect_separation(layout["queue"], layout["analysis"], f"queue overlaps analysis column; screenshot={screenshot_path}")
        self.assertGreater(layout["bodyCard"]["width"], layout["queue"]["width"], f"reading stage should stay wider than queue; screenshot={screenshot_path}")

    def test_reader_layout_breakpoint_matrix(self):
        cases = [
            (1440, 1600, 2, 0, 2),
            (1121, 1800, 2, 0, 2),
            (1120, 1900, 2, 0, 2),
            (901, 2100, 2, 0, 2),
            (900, 2200, 1, 3, 2),
            (640, 2500, 1, 3, 1),
            (390, 2800, 1, 3, 1),
        ]
        for width, height, expected_layout_columns, expected_nav_columns, expected_metric_columns in cases:
            with self.subTest(width=width, height=height):
                layout, screenshot_path = self._capture_page(
                    READER_PAGE,
                    width,
                    height,
                    f"reader-{width}x{height}",
                    READER_READY_SCRIPT,
                    READER_LAYOUT_SCRIPT,
                )
                self.assert_common_reader_invariants(layout, screenshot_path)
                self.assertEqual(layout["layoutColumns"], expected_layout_columns, f"unexpected reader workspace column count; screenshot={screenshot_path}")
                self.assertEqual(layout["navColumns"], expected_nav_columns, f"unexpected reader nav column count; screenshot={screenshot_path}")
                self.assertEqual(layout["metricColumns"], expected_metric_columns, f"unexpected reader metric column count; screenshot={screenshot_path}")
                if width > 1120:
                    self.assert_rect_separation(layout["rail"], layout["shell"], f"sidebar overlaps reader shell above 1120px; screenshot={screenshot_path}")
                else:
                    self.assert_vertical_flow(layout["rail"], layout["shell"], f"sidebar should stack above reader shell at or below 1120px; screenshot={screenshot_path}")
                if expected_layout_columns == 2:
                    self.assert_rect_separation(layout["queue"], layout["analysis"], f"queue overlaps analysis column; screenshot={screenshot_path}")
                else:
                    self.assert_vertical_flow(layout["queue"], layout["analysis"], f"queue should stack above analysis column; screenshot={screenshot_path}")

    def test_reader_layout_survives_search_selection_hash_and_resize(self):
        with PlaywrightSession() as session:
            session.set_window(1440, 1600)
            session.navigate(READER_PAGE.resolve().as_uri())
            self._wait_for_render(session, READER_READY_SCRIPT)

            session.execute(
                """
                const search = document.getElementById('search');
                search.value = 'ai';
                search.dispatchEvent(new Event('input', {bubbles:true}));
                document.getElementById('sort-select').value = 'gaps';
                document.getElementById('sort-select').dispatchEvent(new Event('change', {bubbles:true}));
                """
            )
            self._wait_for_render(session, "return document.querySelector('#stage-title')?.textContent.length > 0;")
            self._save_interaction_screenshot(session, "reader-search-gaps")
            self.assert_common_reader_invariants(session.execute(READER_LAYOUT_SCRIPT), "reader-search-gaps")

            session.execute("document.querySelector('#tier-chips [data-tier=\"1\"]')?.click();")
            self._wait_for_render(session, "return document.querySelector('#stage-tier-chip')?.textContent.includes('Tier 1');")
            self._save_interaction_screenshot(session, "reader-tier1")
            self.assert_common_reader_invariants(session.execute(READER_LAYOUT_SCRIPT), "reader-tier1")

            session.execute(
                """
                const search = document.getElementById('search');
                search.value = 'zzzzzzzz-no-match';
                search.dispatchEvent(new Event('input', {bubbles:true}));
                """
            )
            self._wait_for_render(session, "return !!document.querySelector('#article-body .empty');")
            self._save_interaction_screenshot(session, "reader-empty-state")
            empty_layout = session.execute(READER_LAYOUT_SCRIPT)
            self.assert_no_horizontal_overflow(empty_layout, "reader-empty-state")
            self.assertTrue(empty_layout["bodyHasEmpty"], "reader should render an empty article state when the queue is empty")
            self.assertEqual(empty_layout["queueCardCount"], 0, "queue should have no cards in the empty state")

            session.execute(
                """
                const search = document.getElementById('search');
                search.value = '';
                search.dispatchEvent(new Event('input', {bubbles:true}));
                document.querySelector('#tier-chips [data-tier="all"]')?.click();
                document.getElementById('focus-gaps').click();
                """
            )
            self._wait_for_render(session, "return document.querySelector('#article-list [data-slug]') && document.querySelector('#stage-title')?.textContent.length > 0;")
            session.execute("document.querySelector('#article-list [data-slug]')?.click();")
            self._wait_for_render(session, "return document.querySelector('#reader-companion h2')?.textContent.length > 0;")
            self._save_interaction_screenshot(session, "reader-queue-click")
            self.assert_common_reader_invariants(session.execute(READER_LAYOUT_SCRIPT), "reader-queue-click")

            session.execute("document.querySelector('#article-body .wikilink')?.click();")
            self._wait_for_render(session, "return document.querySelector('#stage-title')?.textContent.length > 0;")
            self._save_interaction_screenshot(session, "reader-wikilink")
            self.assert_common_reader_invariants(session.execute(READER_LAYOUT_SCRIPT), "reader-wikilink")

            stress_slug = session.execute(
                """
                return META.slice()
                  .sort((a, b) => (b.title || '').length - (a.title || '').length)[0].slug;
                """
            )
            session.navigate(f"{READER_PAGE.resolve().as_uri()}#{quote(stress_slug)}")
            self._wait_for_render(session, READER_READY_SCRIPT)
            self._save_interaction_screenshot(session, "reader-hash-stress")
            self.assert_common_reader_invariants(session.execute(READER_LAYOUT_SCRIPT), "reader-hash-stress")

            session.set_window(900, 2200)
            self._wait_for_render(session, READER_READY_SCRIPT)
            self._save_interaction_screenshot(session, "reader-resize-900")
            layout = session.execute(READER_LAYOUT_SCRIPT)
            self.assert_common_reader_invariants(layout, "reader-resize-900")
            self.assertEqual(layout["layoutColumns"], 1, "reader should stack at 900px")

            session.set_window(390, 2800)
            self._wait_for_render(session, READER_READY_SCRIPT)
            self._save_interaction_screenshot(session, "reader-resize-390")
            layout = session.execute(READER_LAYOUT_SCRIPT)
            self.assert_common_reader_invariants(layout, "reader-resize-390")
            self.assertEqual(layout["layoutColumns"], 1, "reader should stay stacked on mobile")

            session.set_window(1440, 1600)
            self._wait_for_render(session, READER_READY_SCRIPT)
            self._save_interaction_screenshot(session, "reader-resize-return")
            layout = session.execute(READER_LAYOUT_SCRIPT)
            self.assert_common_reader_invariants(layout, "reader-resize-return")
            self.assertEqual(layout["layoutColumns"], 2, "reader should restore desktop 2-column workspace")

    def test_index_layout_breakpoint_matrix(self):
        cases = [
            (1440, 1800, 2, 0, 2),
            (1120, 2000, 2, 0, 2),
            (900, 2300, 1, 3, 2),
            (390, 2900, 1, 3, 1),
        ]
        for width, height, expected_layout_columns, expected_nav_columns, expected_metric_columns in cases:
            with self.subTest(width=width, height=height):
                layout, screenshot_path = self._capture_page(
                    INDEX_PAGE,
                    width,
                    height,
                    f"index-{width}x{height}",
                    INDEX_READY_SCRIPT,
                    INDEX_LAYOUT_SCRIPT,
                )
                self.assert_common_index_invariants(layout, screenshot_path)
                self.assertEqual(layout["layoutColumns"], expected_layout_columns, f"unexpected index workspace column count; screenshot={screenshot_path}")
                self.assertEqual(layout["navColumns"], expected_nav_columns, f"unexpected index nav column count; screenshot={screenshot_path}")
                self.assertEqual(layout["metricColumns"], expected_metric_columns, f"unexpected index metric column count; screenshot={screenshot_path}")
                if width > 1120:
                    self.assert_rect_separation(layout["rail"], layout["shell"], f"sidebar overlaps index shell above 1120px; screenshot={screenshot_path}")
                else:
                    self.assert_vertical_flow(layout["rail"], layout["shell"], f"sidebar should stack above index shell at or below 1120px; screenshot={screenshot_path}")
                if expected_layout_columns == 2:
                    self.assert_rect_separation(layout["control"], layout["analysis"], f"index control overlaps analysis column; screenshot={screenshot_path}")
                else:
                    self.assert_vertical_flow(layout["control"], layout["analysis"], f"index control should stack above analysis column; screenshot={screenshot_path}")

    def test_index_layout_survives_filtering_and_resize(self):
        with PlaywrightSession() as session:
            session.set_window(1440, 1800)
            session.navigate(INDEX_PAGE.resolve().as_uri())
            self._wait_for_render(session, INDEX_READY_SCRIPT)

            session.execute(
                """
                const search = document.getElementById('search');
                search.value = 'ai';
                search.dispatchEvent(new Event('input', {bubbles:true}));
                document.querySelector('#tier-chips [data-tier="1"]')?.click();
                document.getElementById('focus-connected').click();
                """
            )
            self._wait_for_render(session, "return document.querySelectorAll('.catalog-card').length > 0;")
            self._save_interaction_screenshot(session, "index-filter-connected")
            self.assert_common_index_invariants(session.execute(INDEX_LAYOUT_SCRIPT), "index-filter-connected")

            session.execute(
                """
                const search = document.getElementById('search');
                search.value = 'zzzzzz-no-match';
                search.dispatchEvent(new Event('input', {bubbles:true}));
                """
            )
            self._wait_for_render(session, "return !!document.querySelector('#catalog-sections .empty');")
            self._save_interaction_screenshot(session, "index-empty-state")
            empty_layout = session.execute(INDEX_LAYOUT_SCRIPT)
            self.assert_no_horizontal_overflow(empty_layout, "index-empty-state")

            session.execute(
                """
                const search = document.getElementById('search');
                search.value = '';
                search.dispatchEvent(new Event('input', {bubbles:true}));
                document.getElementById('focus-gaps').click();
                """
            )
            self._wait_for_render(session, "return document.querySelectorAll('.catalog-card').length > 0;")
            self._save_interaction_screenshot(session, "index-gap-focus")
            self.assert_common_index_invariants(session.execute(INDEX_LAYOUT_SCRIPT), "index-gap-focus")

            session.set_window(390, 2900)
            self._wait_for_render(session, INDEX_READY_SCRIPT)
            self._save_interaction_screenshot(session, "index-resize-390")
            layout = session.execute(INDEX_LAYOUT_SCRIPT)
            self.assert_common_index_invariants(layout, "index-resize-390")
            self.assertEqual(layout["layoutColumns"], 1, "index should stay stacked on mobile")


if __name__ == "__main__":
    unittest.main()
