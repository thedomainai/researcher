/* Researcher — interactions v2(依存なし) */
(function () {
  "use strict";
  var doc = document, root = doc.documentElement;
  var ROOT = root.getAttribute("data-root") || "";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, el) { return (el || doc).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || doc).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  /* ---------- theme ---------- */
  function effectiveTheme() {
    return root.getAttribute("data-theme") || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  }
  $$("[data-theme-toggle]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var next = effectiveTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
      window.dispatchEvent(new Event("themechange"));
    });
  });
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () { window.dispatchEvent(new Event("themechange")); });

  /* ---------- reveal ---------- */
  var hero = $(".hero");
  if (hero) requestAnimationFrame(function () { requestAnimationFrame(function () { hero.classList.add("in"); }); });
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    $$(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- 既読(このブラウザの localStorage にだけ保存する。外部へは送らない) ---------- */
  var art = $("article[data-slug]");
  var HKEY = "rd1", hist = [], readSet = {};
  try { var hv = JSON.parse(localStorage.getItem(HKEY) || "[]"); if (Array.isArray(hv)) hist = hv; } catch (e) {}
  hist.forEach(function (h) { readSet[h[0]] = 1; });
  function paintRead() {
    $$("[data-slug]").forEach(function (el) {
      if (el.tagName === "ARTICLE") return;
      el.classList.toggle("is-read", !!readSet[el.getAttribute("data-slug")]);
    });
  }
  function markRead(slug, title) {
    hist = hist.filter(function (h) { return h[0] !== slug; });
    hist.unshift([slug, title, Date.now()]);
    hist = hist.slice(0, 60);
    readSet[slug] = 1;
    try { localStorage.setItem(HKEY, JSON.stringify(hist)); } catch (e) {}
    paintRead();
  }
  paintRead();
  if (art) {
    var recorded = false, recTitle = ($("h1", art) || {}).textContent || "";
    var record = function () { if (recorded) return; recorded = true; markRead(art.getAttribute("data-slug"), recTitle); };
    setTimeout(record, 6000);
    window.addEventListener("scroll", function () { if (window.scrollY > window.innerHeight * 0.6) record(); }, { passive: true });
  }
  var resume = $(".hero-resume");
  if (resume && hist.length) {
    var last = hist[0];
    $(".mono", resume).textContent = "次の未読";
    $("b", resume).textContent = last[1];
    resume.href = ROOT + "concepts/" + last[0] + "/";
    resume.hidden = false;
    loadIndex().then(function (d) {
      // 最後に読んだ記事と同じ領域で、未読の不変原理(参照の多い順)を「次の一歩」として示す
      var it = bySlugIdx[last[0]]; if (!it) return;
      var pool = d.items.filter(function (x) { return x[4] === it[4] && !readSet[x[0]] && x[5] === 1; }).sort(function (a, b) { return (b[6] || 0) - (a[6] || 0); });
      if (!pool.length) pool = d.items.filter(function (x) { return !readSet[x[0]] && x[5] === 1; }).sort(function (a, b) { return (b[6] || 0) - (a[6] || 0); });
      var nx = pool[0]; if (!nx) return;
      resume.href = ROOT + "concepts/" + nx[0] + "/";
      $(".mono", resume).textContent = "次の未読";
      $("b", resume).textContent = nx[1];
      var why = $(".why", resume); if (why) why.textContent = "前回読んだ「" + last[1] + "」と同じ領域から";
    }).catch(function () {});
  }

  /* ---------- search palette ---------- */
  var palette, pInput, pList, pData = null, pSel = 0, pItems = [];
  function buildPalette() {
    palette = doc.createElement("div");
    palette.className = "palette";
    palette.setAttribute("role", "dialog");
    palette.setAttribute("aria-modal", "true");
    palette.setAttribute("aria-label", "記事を検索");
    palette.innerHTML =
      '<div class="palette-box">' +
      '<div class="palette-in"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="9" r="6"/><path d="M14 14l4 4" stroke-linecap="round"/></svg>' +
      '<input type="text" placeholder="概念・キーワードで探す" autocomplete="off" spellcheck="false" aria-label="検索語"><kbd>ESC</kbd><button class="palette-x" type="button" aria-label="閉じる">×</button></div>' +
      '<ul class="palette-list" role="listbox"></ul>' +
      '<div class="palette-foot mono"><span class="keys">↑↓ 選択 · ↵ 開く</span><span class="palette-n"></span></div></div>';
    doc.body.appendChild(palette);
    pInput = $("input", palette);
    pList = $(".palette-list", palette);
    palette.addEventListener("mousedown", function (e) { if (e.target === palette) closePalette(); });
    pInput.addEventListener("input", renderPalette);
    $(".palette-x", palette).addEventListener("click", closePalette);
    pInput.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); movePalette(1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); movePalette(-1); }
      else if (e.key === "Enter") { e.preventDefault(); var it = pItems[pSel]; if (it) location.href = ROOT + "concepts/" + it[0] + "/"; }
    });
  }
  function openPalette() {
    if (!palette) buildPalette();
    palette.classList.add("on");
    pInput.value = "";
    pInput.focus();
    if (pData) { return renderPalette(); }
    pList.innerHTML = '<li class="palette-none">索引を読み込んでいます…</li>';
    loadIndex().then(renderPalette)
      .catch(function () { pList.innerHTML = '<li class="palette-none">索引を読み込めませんでした</li>'; });
  }
  var idxPromise = null, bySlugIdx = {};
  function loadIndex() {
    if (pData) return Promise.resolve(pData);
    if (!idxPromise) {
      idxPromise = fetch(ROOT + "search.json").then(function (r) { return r.json(); }).then(function (d) {
        pData = d; d.items.forEach(function (it) { bySlugIdx[it[0]] = it; }); return d;
      });
    }
    return idxPromise;
  }
  function closePalette() { if (palette) palette.classList.remove("on"); }
  function movePalette(d) {
    if (!pItems.length) return;
    pSel = (pSel + d + pItems.length) % pItems.length;
    $$("li[role=option]", pList).forEach(function (li, i) { li.classList.toggle("sel", i === pSel); if (i === pSel) li.scrollIntoView({ block: "nearest" }); });
  }
  function mark(text, terms) {
    var out = esc(text);
    terms.forEach(function (t) {
      if (!t) return;
      var re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
      out = out.replace(re, "<mark>$1</mark>");
    });
    return out;
  }
  function renderPalette() {
    if (!pData) return;
    var q = pInput.value.trim().toLowerCase();
    var terms = q.split(/\s+/).filter(Boolean);
    var res, heads = {};
    if (!terms.length) {
      res = []; var seen = {};
      hist.slice(0, 3).forEach(function (h) {
        var it = bySlugIdx[h[0]];
        if (it) { if (!res.length) heads[0] = "最近読んだ記事"; res.push(it); seen[it[0]] = 1; }
      });
      var top = pData.items.filter(function (it) { return it[5] === 1 && !seen[it[0]] && !readSet[it[0]]; })
        .sort(function (a, b) { return (b[6] || 0) - (a[6] || 0); }).slice(0, 6);
      if (top.length) heads[res.length] = "迷ったら、不変原理から";
      res = res.concat(top);
      $(".palette-n", palette).textContent = "おすすめ";
    } else {
      var scored = [];
      for (var i = 0; i < pData.items.length; i++) {
        var it = pData.items[i], t = it[1].toLowerCase(), en = (it[2] || "").toLowerCase(), d = (it[3] || "").toLowerCase(), score = 0, ok = true;
        for (var j2 = 0; j2 < terms.length; j2++) {
          var k = terms[j2], s = 0;
          if (t.indexOf(k) === 0) s = 100; else if (t.indexOf(k) > -1) s = 60; else if (en.indexOf(k) > -1 || it[0].indexOf(k) > -1) s = 40; else if (d.indexOf(k) > -1) s = 10;
          if (!s) { ok = false; break; }
          score += s;
        }
        if (ok) scored.push([score + (it[5] === 1 ? 3 : 0), it]);
      }
      scored.sort(function (a, b) { return b[0] - a[0]; });
      res = scored.slice(0, 40).map(function (x) { return x[1]; });
      $(".palette-n", palette).textContent = scored.length > 40 ? scored.length + " 件中 上位 40 件" : scored.length + " 件";
    }
    pItems = res; pSel = 0;
    if (!res.length) { pList.innerHTML = '<li class="palette-none">「' + esc(pInput.value) + '」に一致する記事はありません</li>'; return; }
    pList.innerHTML = res.map(function (it, i) {
      var c = pData.clusters[it[4]], tm = "", rd = (readSet[it[0]] && !(heads[0] && i < hist.slice(0, 3).length && !terms.length)) ? " is-read" : "";
      return (heads[i] ? '<li class="palette-sec mono" aria-hidden="true">' + esc(heads[i]) + "</li>" : "") +
        '<li role="option" class="' + (i === 0 ? "sel" : "") + rd + '" data-c="' + c[0] + '"><a href="' + ROOT + "concepts/" + it[0] + '/">' +
        '<span class="t">' + mark(it[1], terms) + '</span><span class="m mono"><i class="dot"></i>' + esc(c[1]) + ' <i class="tm" data-t="' + it[5] + '" aria-hidden="true"></i><span class="tl">' + esc((pData.tiers[it[5]] || "").replace(/^\S+\s/, "")) + '</span></span>' +
        '<span class="d">' + esc(it[3]) + "</span></a></li>";
    }).join("");
    $$("li[role=option]", pList).forEach(function (li, i) { li.addEventListener("mousemove", function () { if (pSel !== i) { pSel = i; movePalette(0); } }); });
  }
  $$("[data-search]").forEach(function (b) { b.addEventListener("click", openPalette); });
  doc.addEventListener("keydown", function (e) {
    var typing = /INPUT|TEXTAREA/.test((e.target || {}).tagName || "");
    if ((e.key === "k" || e.key === "K") && (e.metaKey || e.ctrlKey)) { e.preventDefault(); openPalette(); }
    else if (e.key === "/" && !typing) { e.preventDefault(); openPalette(); }
    else if (e.key === "Escape") closePalette();
  });

  /* ---------- list filter ---------- */
  var filters = $(".filters");
  if (filters) {
    var fInput = $("input", filters), fCount = $(".count", filters), fClear = $(".clear", filters), rows = $$(".row"), state = { c: "", t: "" };
    var apply = function () {
      var q = (fInput ? fInput.value : "").trim().toLowerCase(), n = 0;
      rows.forEach(function (r) {
        var ok = (!state.c || r.getAttribute("data-c") === state.c) && (!state.t || r.getAttribute("data-t") === state.t) && (!q || (r.getAttribute("data-s") || "").indexOf(q) > -1);
        r.hidden = !ok; if (ok) n++;
      });
      $$(".group").forEach(function (g) {
        var vis = $$(".row:not([hidden])", g).length, num = $(".n", g);
        g.hidden = !vis;
        if (num) { if (!num.getAttribute("data-all")) num.setAttribute("data-all", num.textContent); num.textContent = (state.c || state.t || q) ? vis + " / " + num.getAttribute("data-all") : num.getAttribute("data-all"); }
      });
      if (fCount) fCount.textContent = n.toLocaleString() + " 件";
      if (fClear) fClear.hidden = !(state.c || state.t || q);
      var empty = $(".empty"); if (empty) empty.hidden = n > 0;
    };
    var syncUrl = function () {
      var u = new URLSearchParams(), qv = (fInput ? fInput.value : "").trim();
      if (state.c) u.set("c", state.c);
      if (state.t) u.set("t", state.t);
      if (qv) u.set("q", qv);
      var qs = u.toString();
      try { history.replaceState(null, "", location.pathname + (qs ? "?" + qs : "") + location.hash); } catch (e) {}
    };
    var apply0 = apply;
    apply = function () { apply0(); syncUrl(); };
    var setChip = function (kind, val) {
      $$('.chip[data-f^="' + kind + ':"]', filters).forEach(function (c) { c.setAttribute("aria-pressed", c.getAttribute("data-f") === kind + ":" + val ? "true" : "false"); });
      state[kind] = val;
    };
    $$(".chip[data-f]", filters).forEach(function (chip) {
      chip.addEventListener("click", function () {
        var kv = chip.getAttribute("data-f").split(":"), on = chip.getAttribute("aria-pressed") === "true";
        setChip(kv[0], on ? "" : kv[1]);
        apply();
      });
    });
    if (fInput) fInput.addEventListener("input", apply);
    if (fClear) fClear.addEventListener("click", function () {
      state.c = ""; state.t = ""; if (fInput) fInput.value = "";
      $$(".chip[data-f]", filters).forEach(function (c) { c.setAttribute("aria-pressed", "false"); });
      apply();
    });
    var qp = new URLSearchParams(location.search);
    if (qp.get("c") && $('.chip[data-f="c:' + qp.get("c") + '"]', filters)) setChip("c", qp.get("c"));
    if (/^[123]$/.test(qp.get("t") || "")) setChip("t", qp.get("t"));
    if (fInput && qp.get("q")) fInput.value = qp.get("q");
    if (state.c || state.t || (fInput && fInput.value)) apply();
  }

  /* ---------- 本文中のリンクのプレビュー(ホバー・フォーカス時) ---------- */
  var pv = null, pvTimer = 0, pvFor = null;
  var canHover = window.matchMedia("(hover: hover)").matches;
  function hidePreview() { pvFor = null; clearTimeout(pvTimer); if (pv) pv.classList.remove("on"); }
  function showPreview(a) {
    var slug = a.getAttribute("data-slug");
    if (!slug || (art && slug === art.getAttribute("data-slug"))) return;
    pvFor = a;
    loadIndex().then(function () {
      var it = bySlugIdx[slug];
      if (!it || pvFor !== a) return;
      if (!pv) { pv = doc.createElement("div"); pv.className = "pv"; pv.setAttribute("role", "tooltip"); doc.body.appendChild(pv); }
      var c = pData.clusters[it[4]];
      pv.setAttribute("data-c", c[0]);
      pv.innerHTML = '<span class="mono"><i class="dot"></i>' + esc(c[1]) + ' · <i class="tm" data-t="' + it[5] + '" aria-hidden="true"></i>' + esc((pData.tiers[it[5]] || "").replace(/^\S+\s/, "")) + (readSet[slug] ? " · 既読" : "") +
        "</span><b>" + esc(it[1]) + '</b><span class="d">' + esc(it[3]) + '</span><span class="mono go">クリックで開く →</span>';
      var r = a.getBoundingClientRect(), w = Math.min(340, window.innerWidth - 24);
      pv.style.width = w + "px";
      pv.classList.add("on");
      var h = pv.offsetHeight, below = r.bottom + h + 16 < window.innerHeight;
      pv.style.left = Math.max(12, Math.min(r.left + window.scrollX, window.scrollX + window.innerWidth - w - 12)) + "px";
      pv.style.top = (below ? r.bottom + window.scrollY + 8 : r.top + window.scrollY - h - 8) + "px";
    }).catch(function () {});
  }
  if (canHover) {
    doc.addEventListener("mouseover", function (e) {
      var a = e.target.closest ? e.target.closest("a.wikilink[data-slug]") : null;
      if (!a || a === pvFor) return;
      clearTimeout(pvTimer); pvTimer = setTimeout(function () { showPreview(a); }, 220);
    });
    doc.addEventListener("mouseout", function (e) {
      var a = e.target.closest ? e.target.closest("a.wikilink[data-slug]") : null;
      if (a && !(e.relatedTarget && a.contains(e.relatedTarget))) hidePreview();
    });
  }
  doc.addEventListener("focusin", function (e) { if (e.target.matches && e.target.matches("a.wikilink[data-slug]")) showPreview(e.target); });
  doc.addEventListener("focusout", function (e) { if (e.target.matches && e.target.matches("a.wikilink[data-slug]")) hidePreview(); });
  doc.addEventListener("keydown", function (e) { if (e.key === "Escape") hidePreview(); });

  /* ---------- 記事末尾(モバイル): 各列の 2 本目以降を畳む ---------- */
  $$(".next-col").forEach(function (col) {
    var rest = $$(".more-row", col);
    if (!rest.length) return;
    var li = doc.createElement("li"); li.className = "more-toggle";
    li.innerHTML = '<button type="button" aria-expanded="false">残り ' + rest.length + " 本を見る +</button>";
    $("ul", col).appendChild(li);
    $("button", li).addEventListener("click", function () {
      var open = col.classList.toggle("is-open");
      this.setAttribute("aria-expanded", open ? "true" : "false");
      this.textContent = open ? "閉じる −" : "残り " + rest.length + " 本を見る +";
    });
  });

  /* ---------- 本文の終わりの受け渡し(出典の直前) ---------- */
  var handoff = $("[data-handoff]");
  if (handoff && $(".next-main")) {
    var hc = []; try { hc = JSON.parse($(".next-main").getAttribute("data-cands") || "[]"); } catch (e) {}
    var hp = hc.filter(function (c) { return !readSet[c[0]]; })[0] || hc[0];
    if (hp) { var hn = $(".hf-next", handoff); hn.href = ROOT + "concepts/" + hp[0] + "/"; hn.innerHTML = "次に読む: <b>" + esc(hp[1]) + "</b> →"; handoff.hidden = false; }
  }

  /* ---------- 読了間際の「次に読む」バー ---------- */
  var nbar = $(".next-bar");
  if (nbar && art) {
    var cands = [], nbDismissed = false, nbRoot = nbar.getAttribute("data-root") || ROOT;
    try { cands = JSON.parse(nbar.getAttribute("data-cands") || "[]"); } catch (e) {}
    try { nbDismissed = sessionStorage.getItem("nb-off") === "1"; } catch (e) {}
    var pick = cands.filter(function (c) { return !readSet[c[0]]; })[0] || cands[0];
    if (pick) {
      var nl = $("a", nbar); nl.href = nbRoot + "concepts/" + pick[0] + "/"; $("b", nl).textContent = pick[1];
      var nextSec = $(".next"), proseEl = $(".prose");
      var srcHead = $("#sources"), shareEl = $(".side-meta .share"), noticeEl = $(".notice");
      var inView = function (el) { if (!el) return false; var r = el.getBoundingClientRect(); return r.top < window.innerHeight * 0.92 && r.bottom > 0; };
      var nbUpdate = function () {
        if (nbDismissed) { nbar.classList.remove("on"); return; }
        var vh = window.innerHeight, show;
        var nr = nextSec ? nextSec.getBoundingClientRect() : null;
        var nextVisible = nr && nr.top < vh * 0.7;
        if (srcHead) {
          // 本文を読み終える手前(出典の見出しが画面の下から近づいてきた間)だけ出す
          var st = srcHead.getBoundingClientRect().top;
          show = st > vh * 0.92 && st < vh * 1.9 && !nextVisible;
        } else {
          var pr = proseEl.getBoundingClientRect();
          var past = (vh - pr.top) / Math.max(1, pr.height) > 0.72;
          show = past && !nextVisible && !inView(noticeEl);
        }
        var sidebarFixed = window.innerWidth > 1080;
        if (show && !sidebarFixed && inView(shareEl)) show = false;
        nbar.hidden = false;
        nbar.classList.toggle("on", show);
      };
      window.addEventListener("scroll", nbUpdate, { passive: true }); window.addEventListener("resize", nbUpdate); nbUpdate();
      $("button", nbar).addEventListener("click", function () { nbDismissed = true; try { sessionStorage.setItem("nb-off", "1"); } catch (e) {} nbUpdate(); });
    }
  }

  /* ---------- article ---------- */
  var progress = $(".progress");
  if (progress) {
    var prose = $(".prose");
    var onScroll = function () {
      var r = prose.getBoundingClientRect(), total = r.height - window.innerHeight * 0.6;
      var p = Math.max(0, Math.min(1, (-r.top + window.innerHeight * 0.3) / Math.max(1, total)));
      progress.style.transform = "scaleX(" + p + ")";
    };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
    var links = $$(".side-toc .toc a"), heads = $$(".prose h2[id]");
    if (links.length) {
      var map = {}; links.forEach(function (a) { map[decodeURIComponent(a.hash.slice(1))] = a; });
      var cur = null, mark = function () {
        var line = window.innerHeight * 0.3, found = heads[0];
        for (var i = 0; i < heads.length; i++) { if (heads[i].getBoundingClientRect().top <= line) found = heads[i]; else break; }
        if (found && found !== cur) { cur = found; links.forEach(function (a) { a.classList.remove("on"); }); var a = map[found.id]; if (a) a.classList.add("on"); }
      };
      window.addEventListener("scroll", mark, { passive: true }); mark();
    }
  }
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var done = function () { var o = b.textContent; b.textContent = "コピーしました"; setTimeout(function () { b.textContent = o; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(done); else done();
    });
  });

  /* ---------- graph engine ---------- */
  function isDark() { return effectiveTheme() === "dark"; }
  function clusterColors(keys) {
    var probe = doc.createElement("i"); doc.body.appendChild(probe);
    var out = keys.map(function (k) { probe.setAttribute("data-c", k); return getComputedStyle(probe).getPropertyValue("--c").trim() || "#888"; });
    var cs = getComputedStyle(root);
    out.ink = cs.getPropertyValue("--ink").trim(); out.ink2 = cs.getPropertyValue("--ink-2").trim(); out.paper = cs.getPropertyValue("--paper").trim();
    probe.remove();
    return out;
  }
  function Graph(canvas, data, opt) {
    var ctx = canvas.getContext("2d"), W = 0, H = 0, dpr = 1, self = this;
    var keys = data.clusters.map(function (c) { return c[0]; }), colors = clusterColors(keys);
    var K = keys.length, R0 = opt.ring, G = opt.cell;
    var seed = 7; var rnd = function () { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
    var anchors = keys.map(function (_, i) { var a = -Math.PI / 2 + (Math.PI * 2 * i) / K + 0.3; return [Math.cos(a) * R0 * (opt.aspect || 1), Math.sin(a) * R0]; });
    var N = data.nodes.map(function (n, i) {
      var a = anchors[n[2]], ang = rnd() * 6.283, rad = Math.sqrt(rnd()) * Math.max(R0, opt.spread || 0) * 0.7;
      return { i: i, slug: n[0], title: n[1], c: n[2], tier: n[3], deg: n[4], desc: n[5] || "", x: a[0] + Math.cos(ang) * rad, y: a[1] + Math.sin(ang) * rad, vx: 0, vy: 0, r: opt.r0 + Math.sqrt(n[4]) * opt.rk, ph: rnd() * 6.283, adj: [] };
    });
    if (opt.pin != null && N[opt.pin]) { N[opt.pin].x = 0; N[opt.pin].y = 0; N[opt.pin].r = opt.pinR || N[opt.pin].r; }
    var E = data.edges.filter(function (e) { return N[e[0]] && N[e[1]]; });
    E.forEach(function (e) { N[e[0]].adj.push(e[1]); N[e[1]].adj.push(e[0]); });
    var hidden = {}, hiddenT = {}, hover = null, selected = null, view = { s: 1, x: 0, y: 0 }, fitS = 1, alpha = 1, t0 = performance.now(), visible = true, raf = 0, frame = 0;
    var regionSet = {}; (opt.regions || []).forEach(function (r) { regionSet[r.replace(/\s/g, "")] = 1; });
    var labelRank = N.filter(function (n) { return n.title.length <= (opt.labelMax || 99) && !regionSet[n.title.replace(/\s/g, "")]; }).sort(function (a, b) { return b.deg - a.deg; });
    if (opt.perCluster) {
      var buckets = keys.map(function () { return []; }), mixed = [];
      labelRank.forEach(function (n) { buckets[n.c].push(n); });
      for (var bi = 0; bi < 40; bi++) buckets.forEach(function (b) { if (b[bi]) mixed.push(b[bi]); });
      labelRank = mixed;
    }
    if (opt.pin != null) labelRank = N.slice().sort(function (a, b) { return (b.i === opt.pin) - (a.i === opt.pin) || b.deg - a.deg; });
    var labelCache = null, labelKey = "";

    function off(n) { return hidden[n.c] || hiddenT[n.tier]; }
    function tick() {
      var grid = {}, i, n, key;
      for (i = 0; i < N.length; i++) { n = N[i]; key = ((n.x / G) | 0) + ":" + ((n.y / G) | 0); (grid[key] || (grid[key] = [])).push(n); }
      for (i = 0; i < N.length; i++) {
        n = N[i];
        var gx = (n.x / G) | 0, gy = (n.y / G) | 0;
        for (var dx = -1; dx <= 1; dx++) for (var dy = -1; dy <= 1; dy++) {
          var cell = grid[(gx + dx) + ":" + (gy + dy)]; if (!cell) continue;
          for (var j = 0; j < cell.length; j++) {
            var m = cell[j]; if (m.i <= n.i) continue;
            var ex = n.x - m.x, ey = n.y - m.y, d = Math.sqrt(ex * ex + ey * ey) || 0.01, min = G * 0.62 + n.r + m.r;
            if (d < min) { var f = ((min - d) / d) * 0.16 * alpha; n.vx += ex * f; n.vy += ey * f; m.vx -= ex * f; m.vy -= ey * f; }
          }
        }
        var a = anchors[n.c];
        n.vx += (a[0] - n.x) * opt.gravity * alpha; n.vy += (a[1] - n.y) * opt.gravity * alpha;
      }
      for (i = 0; i < E.length; i++) {
        var p = N[E[i][0]], q = N[E[i][1]], lx = q.x - p.x, ly = q.y - p.y, ld = Math.sqrt(lx * lx + ly * ly) || 0.01;
        var lf = ((ld - opt.link) / ld) * opt.spring * alpha; lx *= lf; ly *= lf;
        p.vx += lx; p.vy += ly; q.vx -= lx; q.vy -= ly;
      }
      for (i = 0; i < N.length; i++) {
        n = N[i];
        if (opt.pin === n.i) { n.x = 0; n.y = 0; n.vx = 0; n.vy = 0; continue; }
        n.vx *= 0.8; n.vy *= 0.8; n.x += n.vx; n.y += n.vy;
      }
      alpha *= 0.992;
    }
    for (var w = 0; w < opt.warm; w++) tick();

    var regionExt = anchors.map(function (a, ci) {
      var al = Math.sqrt(a[0] * a[0] + a[1] * a[1]) || 1, m = 0;
      N.forEach(function (n) { if (n.c === ci) { var d = (n.x * a[0] + n.y * a[1]) / al; if (d > m) m = d; } });
      return m;
    });
    var regionMid = anchors.map(function (a, ci) {
      var sxm = 0, sym = 0, k = 0; N.forEach(function (n) { if (n.c === ci) { sxm += n.x; sym += n.y; k++; } });
      return k ? [sxm / k, sym / k] : a;
    });
    function resize() {
      var r = canvas.getBoundingClientRect(); dpr = Math.min(2, window.devicePixelRatio || 1);
      W = r.width; H = r.height; canvas.width = W * dpr; canvas.height = H * dpr;
      if (!self.userMoved) fit();
    }
    function fit() {
      var x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
      N.forEach(function (n) { if (n.x < x0) x0 = n.x; if (n.x > x1) x1 = n.x; if (n.y < y0) y0 = n.y; if (n.y > y1) y1 = n.y; });
      var pad = opt.pad || 60, pl = opt.padL != null ? opt.padL() : pad, pt = opt.padT != null ? opt.padT() : pad, pb = opt.padB != null ? opt.padB : pad;
      var s = Math.min((W - pl - pad) / Math.max(1, x1 - x0), (H - pt - pb) / Math.max(1, y1 - y0));
      view.s = Math.max(0.05, Math.min(opt.maxFit || 9, s)); fitS = view.s;
      view.x = pl + (W - pl - pad) / 2 - ((x0 + x1) / 2) * view.s; view.y = pt + (H - pt - pb) / 2 - ((y0 + y1) / 2) * view.s;
    }
    function sx(n, t) { return (n.x + (reduce ? 0 : Math.sin(t * 0.00042 + n.ph) * opt.drift)) * view.s + view.x; }
    function sy(n, t) { return (n.y + (reduce ? 0 : Math.cos(t * 0.00037 + n.ph * 1.7) * opt.drift)) * view.s + view.y; }
    function zscale() { return Math.max(0.55, Math.min(1.9, Math.sqrt(view.s))); }

    function layoutLabels(t, focus) {
      var zs = zscale(), avoid = opt.avoid ? opt.avoid() : [], shown = [], out = [], i, n;
      var max = focus ? 16 : opt.labels(view.s / fitS);
      if (!focus) regionBoxes().forEach(function (b) { if (b) shown.push([b[0] - b[2] / 2 - 10, b[1] - 20, b[0] + b[2] / 2 + 10, b[1] + 20]); });
      var cand = focus ? [focus].concat(focus.adj.map(function (j) { return N[j]; }).sort(function (a, b) { return b.deg - a.deg; })) : labelRank;
      var pts = [];
      for (i = 0; i < N.length; i++) { n = N[i]; if (off(n)) continue; var px = sx(n, t), py = sy(n, t); if (px > -20 && py > -20 && px < W + 20 && py < H + 20) pts.push([px, py, n.r * zs, n.i]); }
      for (i = 0; i < cand.length && out.length < max; i++) {
        n = cand[i]; if (off(n)) continue;
        var x = sx(n, t), y = sy(n, t); if (x < 0 || y < 0 || x > W || y > H) continue;
        var must = n === focus, big = n === selected || (opt.pin === n.i) || (must && !opt.regions), fs = big ? 15 : (must ? 13.5 : 12.5);
        ctx.font = (big ? "700 " : "600 ") + fs + 'px "Shippori Mincho B1","Hiragino Mincho ProN",serif';
        var cap = focus ? 30 : 20, label = n.title.length > cap ? n.title.slice(0, cap - 1) + "…" : n.title, tw = ctx.measureText(label).width, rr = n.r * zs + 7;
        var opts = [[x + rr, y, 0], [x - rr - tw, y, 1], [x - tw / 2, y - rr - 8, 2], [x - tw / 2, y + rr + 8, 3]], placed = null;
        var ref = focus && n !== focus ? focus : (opt.pin != null && n.i !== opt.pin ? N[opt.pin] : null);
        if (ref) {
          var ddx = x - sx(ref, t), ddy = y - sy(ref, t);
          if (Math.abs(ddx) >= Math.abs(ddy)) { if (ddx < 0) opts = [opts[1], opts[2], opts[3], opts[0]]; }
          else opts = ddy < 0 ? [opts[2], opts[0], opts[1], opts[3]] : [opts[3], opts[0], opts[1], opts[2]];
        }
        if (big) {
          var bestK = 0, bestHits = 1e9;
          for (var kk = 0; kk < opts.length; kk++) {
            var bb = [opts[kk][0] - 9, opts[kk][1] - 16, opts[kk][0] + tw + 9, opts[kk][1] + 16], hh = 0;
            if (bb[0] < 2 || bb[2] > W - 2) hh += 50;
            for (var pp = 0; pp < pts.length; pp++) { var q2 = pts[pp]; if (q2[3] !== n.i && q2[0] + q2[2] > bb[0] && q2[0] - q2[2] < bb[2] && q2[1] + q2[2] > bb[1] && q2[1] - q2[2] < bb[3]) hh++; }
            if (hh < bestHits) { bestHits = hh; bestK = kk; }
          }
          opts = [opts[bestK]];
        }
        for (var k = 0; k < opts.length && !placed; k++) {
          var bx = opts[k][0], by = opts[k][1], box = [bx - 3, by - 10, bx + tw + 3, by + 10], bad = false, s;
          if (!big && !must && (box[0] < 4 || box[2] > W - 4 || box[1] < 4 || box[3] > H - 4)) continue;
          for (s = 0; s < shown.length && !bad; s++) { var b = shown[s]; if (box[0] < b[2] && box[2] > b[0] && box[1] < b[3] && box[3] > b[1]) bad = true; }
          for (s = 0; s < avoid.length && !bad; s++) { var a = avoid[s]; if (box[0] < a[2] && box[2] > a[0] && box[1] < a[3] && box[3] > a[1]) bad = true; }
          if (must && !big) { bad = false; }
          if (!bad && !big && !must) {
            var hits = 0;
            for (s = 0; s < pts.length; s++) { var p = pts[s]; if (p[3] === n.i) continue; if (p[0] + p[2] + 5 > box[0] && p[0] - p[2] - 5 < box[2] && p[1] + p[2] + 5 > box[1] && p[1] - p[2] - 5 < box[3]) { hits++; if (hits > (opt.labelHits || 0)) { bad = true; break; } } }
          }
          if (!bad) { placed = opts[k]; shown.push(box); }
        }
        if (placed) out.push({ n: n, side: placed[2], label: label, tw: tw, big: big, fs: fs });
      }
      return out;
    }

    function regionBoxes() {
      var out = [], rel = view.s / fitS;
      if (!opt.regions || rel >= 2.2) return out;
      ctx.font = '700 ' + Math.round(Math.max(15, Math.min(30, (opt.regionsOnTop ? 16 : 21) * rel))) + 'px "Shippori Mincho B1","Hiragino Mincho ProN",serif';
      var av = opt.avoid ? opt.avoid() : [];
      for (var ci = 0; ci < K; ci++) {
        if (hidden[ci]) { out.push(null); continue; }
        var a = anchors[ci], al = Math.sqrt(a[0] * a[0] + a[1] * a[1]) || 1, ux = a[0] / al, uy = a[1] / al, cx2, cy2, tw = ctx.measureText(opt.regions[ci]).width;
        if (opt.regionsOnTop) { cx2 = regionMid[ci][0] * view.s + view.x; cy2 = regionMid[ci][1] * view.s + view.y; }
        else { cx2 = ux * regionExt[ci] * view.s + view.x + ux * (26 + tw / 2); cy2 = uy * regionExt[ci] * view.s + view.y + uy * 28; }
        cx2 = Math.max(tw / 2 + 8, Math.min(W - tw / 2 - 8, cx2)); cy2 = Math.max(18, Math.min(H - 18, cy2));
        av.forEach(function (r) { if (cx2 - tw / 2 < r[2] + 14 && cx2 + tw / 2 > r[0] - 14 && cy2 + 16 > r[1] - 14 && cy2 - 16 < r[3] + 14) { if (cy2 > (r[1] + r[3]) / 2) cy2 = r[3] + 34; else cx2 = r[2] + 20 + tw / 2; } });
        out.push([cx2, cy2, tw]);
      }
      return out;
    }
    function drawRegions() {
      var rel = view.s / fitS, ra = Math.max(0, Math.min(1, (2.2 - rel) / 1.0));
      if (ra <= 0) return;
      var boxes = regionBoxes();
      ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.lineJoin = "round";
      ctx.font = '700 ' + Math.round(Math.max(15, Math.min(30, (opt.regionsOnTop ? 16 : 21) * rel))) + 'px "Shippori Mincho B1","Hiragino Mincho ProN",serif';
      boxes.forEach(function (b, ci) {
        if (!b) return;
        ctx.globalAlpha = ra; ctx.strokeStyle = colors.paper; ctx.lineWidth = opt.regionsOnTop ? 8 : 6; ctx.strokeText(opt.regions[ci], b[0], b[1]);
        ctx.fillStyle = opt.regionsOnTop ? colors.ink : colors[ci]; ctx.fillText(opt.regions[ci], b[0], b[1]);
      });
      ctx.textAlign = "left"; ctx.globalAlpha = 1;
    }
    function drawRegionsOld() {
      var rel = view.s / fitS, ra = 0;
      if (ra <= 0) return;
      ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.lineJoin = "round";
      ctx.font = '700 ' + Math.round(Math.max(15, Math.min(30, (opt.regionsOnTop ? 16 : 21) * rel))) + 'px "Shippori Mincho B1","Hiragino Mincho ProN",serif';
      for (var ci = 0; ci < K; ci++) {
        if (hidden[ci]) continue;
        var a = anchors[ci], al = Math.sqrt(a[0] * a[0] + a[1] * a[1]) || 1, ux = a[0] / al, uy = a[1] / al, cx2, cy2, tw = ctx.measureText(opt.regions[ci]).width;
        if (opt.regionsOnTop) { cx2 = regionMid[ci][0] * view.s + view.x; cy2 = regionMid[ci][1] * view.s + view.y; }
        else { cx2 = ux * regionExt[ci] * view.s + view.x + ux * (26 + tw / 2); cy2 = uy * regionExt[ci] * view.s + view.y + uy * 28; }
        cx2 = Math.max(tw / 2 + 8, Math.min(W - tw / 2 - 8, cx2)); cy2 = Math.max(18, Math.min(H - 18, cy2));
        (opt.avoid ? opt.avoid() : []).forEach(function (r) { if (cx2 - tw / 2 < r[2] + 14 && cx2 + tw / 2 > r[0] - 14 && cy2 + 16 > r[1] - 14 && cy2 - 16 < r[3] + 14) { if (cy2 > (r[1] + r[3]) / 2) cy2 = r[3] + 34; else cx2 = r[2] + 20 + tw / 2; } });
        ctx.globalAlpha = ra; ctx.strokeStyle = colors.paper; ctx.lineWidth = opt.regionsOnTop ? 8 : 6; ctx.strokeText(opt.regions[ci], cx2, cy2);
        ctx.globalAlpha = ra; ctx.fillStyle = opt.regionsOnTop ? colors.ink : colors[ci]; ctx.fillText(opt.regions[ci], cx2, cy2);
      }
      ctx.textAlign = "left"; ctx.globalAlpha = 1;
    }

    function draw(now) {
      var t = now - t0, i, n, focus = hover || selected, zs = zscale(), filtering = !!(hiddenT[1] || hiddenT[2] || hiddenT[3]);
      frame++;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      var near = {}; if (focus) { near[focus.i] = 1; focus.adj.forEach(function (j) { near[j] = 1; }); }
      var ea = opt.edgeAlpha * (isDark() ? 1.9 : 1) / Math.max(1, Math.pow(view.s / fitS, 1.1));
      ctx.lineWidth = 0.8; ctx.strokeStyle = colors.ink; ctx.globalAlpha = focus ? ea * 0.35 : ea; ctx.beginPath();
      for (i = 0; i < E.length; i++) {
        var p = N[E[i][0]], q = N[E[i][1]]; if (off(p) || off(q)) continue;
        ctx.moveTo(sx(p, t), sy(p, t)); ctx.lineTo(sx(q, t), sy(q, t));
      }
      ctx.stroke();
      if (focus) {
        ctx.globalAlpha = 0.6; ctx.strokeStyle = colors[focus.c]; ctx.lineWidth = 1.1; ctx.beginPath();
        focus.adj.forEach(function (j) { var m = N[j]; if (off(m)) return; ctx.moveTo(sx(focus, t), sy(focus, t)); ctx.lineTo(sx(m, t), sy(m, t)); });
        ctx.stroke();
      }
      if (opt.regions && !focus && !opt.regionsOnTop) drawRegions();
      for (i = 0; i < N.length; i++) {
        n = N[i]; if (off(n)) continue;
        var x = sx(n, t), y = sy(n, t); if (x < -30 || y < -30 || x > W + 30 || y > H + 30) continue;
        var r = n.r * zs * (n === focus ? 1.45 : 1);
        ctx.globalAlpha = focus ? (near[n.i] ? 1 : 0.14) : (n.tier === 1 ? 0.95 : 0.62);
        ctx.fillStyle = colors[n.c]; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.283); ctx.fill();
        if (filtering) { ctx.strokeStyle = colors.ink; ctx.lineWidth = 1; ctx.globalAlpha = Math.min(1, ctx.globalAlpha + 0.1); ctx.stroke(); }
        if (n === selected || (opt.pin === n.i && !focus)) { ctx.globalAlpha = 1; ctx.strokeStyle = colors.ink; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(x, y, r + 4.5, 0, 6.283); ctx.stroke(); }
      }
      if (opt.regions && !focus && opt.regionsOnTop) drawRegions();
      var key = [view.s.toFixed(3), view.x | 0, view.y | 0, focus ? focus.i : -1, W | 0, H | 0, Object.keys(hidden).filter(function (k) { return hidden[k]; }).join(","), Object.keys(hiddenT).filter(function (k) { return hiddenT[k]; }).join(",")].join("|");
      if (!labelCache || key !== labelKey || frame % 90 === 0 || alpha > 0.05) { labelCache = layoutLabels(t, focus); labelKey = key; }
      ctx.textBaseline = "middle"; ctx.lineJoin = "round";
      for (i = 0; i < labelCache.length; i++) {
        var L = labelCache[i]; n = L.n;
        var lx = sx(n, t), ly = sy(n, t), rr = n.r * zs * (n === focus ? 1.45 : 1) + (L.big ? 12 : 7), bx, by;
        if (L.side === 0) { bx = lx + rr; by = ly; } else if (L.side === 1) { bx = lx - rr - L.tw; by = ly; } else if (L.side === 2) { bx = lx - L.tw / 2; by = ly - rr - 8; } else { bx = lx - L.tw / 2; by = ly + rr + 8; }
        bx = Math.max(8, Math.min(W - L.tw - 12, bx));
        ctx.font = (L.big ? "700 " : "600 ") + L.fs + 'px "Shippori Mincho B1","Hiragino Mincho ProN",serif';
        ctx.globalAlpha = 1; ctx.strokeStyle = colors.paper; ctx.lineWidth = 5; ctx.strokeText(L.label, bx, by + 1);
        ctx.globalAlpha = 1; ctx.fillStyle = colors.ink; ctx.fillText(L.label, bx, by + 1);
      }
      ctx.globalAlpha = 1;
    }
    function loop(now) {
      raf = 0; if (!visible) return;
      if (alpha > 0.05) { tick(); if (!self.userMoved && opt.refit) fit(); }
      draw(now);
      if (!reduce || alpha > 0.05) raf = requestAnimationFrame(loop);
    }
    function kick() { if (!raf) raf = requestAnimationFrame(loop); }
    function pick(px, py) {
      var best = null, bd = 1e9, t = performance.now() - t0, zs = zscale();
      for (var i = 0; i < N.length; i++) {
        var n = N[i]; if (off(n)) continue;
        var dx = sx(n, t) - px, dy = sy(n, t) - py, d = dx * dx + dy * dy, lim = Math.max(13, n.r * zs + 8);
        if (d < lim * lim && d < bd) { bd = d; best = n; }
      }
      return best;
    }
    this.nodes = N; this.view = view;
    this.pick = pick; this.kick = kick; this.fit = function () { self.userMoved = false; fit(); kick(); };
    this.setHover = function (n) { if (hover !== n) { hover = n; kick(); } };
    this.select = function (n) { selected = n; kick(); };
    this.toggle = function (c, on) { hidden[c] = !on; kick(); };
    this.toggleTier = function (t, on) { hiddenT[t] = !on; kick(); };
    this.pos = function (n) { var t = performance.now() - t0; return [sx(n, t), sy(n, t)]; };
    this.zoom = function (f, px, py) {
      px = px == null ? W / 2 : px; py = py == null ? H / 2 : py;
      var ns = Math.max(fitS * 0.6, Math.min(fitS * 14, view.s * f)); f = ns / view.s;
      view.x = px - (px - view.x) * f; view.y = py - (py - view.y) * f; view.s = ns; self.userMoved = true; kick();
    };
    this.pan = function (dx, dy) { view.x += dx; view.y += dy; self.userMoved = true; kick(); };
    this.center = function (n, mult, ox, oy) { if (mult) view.s = fitS * mult; view.x = (ox == null ? W / 2 : ox) - n.x * view.s; view.y = (oy == null ? H / 2 : oy) - n.y * view.s; self.userMoved = true; kick(); };
    this.size = function () { return [W, H]; };
    this.frame = function (n, box) {
      var x0 = n.x, x1 = n.x, y0 = n.y, y1 = n.y;
      n.adj.forEach(function (j) { var m = N[j]; if (off(m)) return; if (m.x < x0) x0 = m.x; if (m.x > x1) x1 = m.x; if (m.y < y0) y0 = m.y; if (m.y > y1) y1 = m.y; });
      var bw = box[2] - box[0], bh = box[3] - box[1];
      view.s = Math.max(fitS * 0.4, Math.min(fitS * 3.2, Math.min(bw / Math.max(60, x1 - x0), bh / Math.max(60, y1 - y0))));
      view.x = box[0] + bw / 2 - ((x0 + x1) / 2) * view.s; view.y = box[1] + bh / 2 - ((y0 + y1) / 2) * view.s; self.userMoved = true; kick();
    };
    window.addEventListener("resize", function () { resize(); kick(); });
    window.addEventListener("themechange", function () { colors = clusterColors(keys); kick(); });
    doc.addEventListener("visibilitychange", function () { visible = !doc.hidden; if (visible) kick(); });
    if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { visible = es[0].isIntersecting && !doc.hidden; if (visible) kick(); }).observe(canvas);
    if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(function () { labelCache = null; kick(); });
    resize(); kick();
  }

  /* 小さなグラフ(ホームと記事ヘッダー): ホバーで名前、クリックで記事へ */
  function mountMini(canvas, data, opt) {
    var tip = $(".graph-tip", canvas.parentNode), g = new Graph(canvas, data, opt), hov = null;
    canvas.addEventListener("pointermove", function (e) {
      var r = canvas.getBoundingClientRect(), n = g.pick(e.clientX - r.left, e.clientY - r.top);
      if (n && opt.pin === n.i) n = null;
      hov = n; g.setHover(n); canvas.style.cursor = n ? "pointer" : "default";
      if (n && tip) {
        var p = g.pos(n);
        tip.innerHTML = "<small>" + esc(data.clusters[n.c][1]) + "</small>" + esc(n.title) + (n.desc ? "<p>" + esc(n.desc) + "</p>" : "") + "<em>クリックで記事へ →</em>";
        var below = p[1] < 190;
        tip.style.transform = below ? "translate(-50%, 18px)" : "";
        tip.style.left = Math.max(156, Math.min(r.width - 156, p[0])) + "px"; tip.style.top = p[1] + "px"; tip.classList.add("on");
      } else if (tip) tip.classList.remove("on");
    });
    canvas.addEventListener("pointerleave", function () { hov = null; g.setHover(null); if (tip) tip.classList.remove("on"); });
    canvas.addEventListener("click", function () { if (hov) location.href = ROOT + "concepts/" + hov.slug + "/"; });
    return g;
  }
  var heroCanvas = $(".hero-canvas canvas"), heroData = $("#hero-graph");
  if (heroCanvas && heroData) {
    mountMini(heroCanvas, JSON.parse(heroData.textContent), {
      ring: 190, cell: 54, r0: 3.2, rk: 1.25, gravity: 0.02, link: 70, spring: 0.012, warm: reduce ? 260 : 46, drift: 5, edgeAlpha: 0.13, refit: true,
      pad: 44, padB: 64, aspect: 0.95, labelMax: 13, perCluster: true,
      avoid: function () { var r = heroCanvas.getBoundingClientRect(); return window.innerWidth > 900 ? [[0, 0, r.width * 0.2, r.height], [0, r.height - 44, r.width, r.height]] : []; },
      labels: function () { return window.innerWidth > 900 ? 7 : 4; }
    });
  }
  var egoCanvas = $(".ego canvas"), egoData = $("#ego-graph");
  if (egoCanvas && egoData && egoCanvas.offsetParent) {
    mountMini(egoCanvas, JSON.parse(egoData.textContent), {
      ring: 0, spread: 90, cell: 52, r0: 3.4, rk: 0.9, gravity: 0.03, link: 92, spring: 0.03, warm: 240, drift: 2.2, edgeAlpha: 0.22, refit: true,
      pad: 30, padB: 40, maxFit: 1.5, pin: 0, pinR: 9, labelHits: 0,
      labels: function () { return 5; }
    });
  }

  /* atlas */
  var atlas = $(".atlas");
  if (atlas) {
    var ac = $("canvas", atlas), card = $(".atlas-card", atlas), panel = $(".atlas-panel", atlas), zoomBox = $(".atlas-zoom", atlas);
    var rectOf = function (el, pad) { var a = ac.getBoundingClientRect(), r = el.getBoundingClientRect(); return [r.left - a.left - pad, r.top - a.top - pad, r.right - a.left + pad, r.bottom - a.top + pad]; };
    fetch(ROOT + "graph.json").then(function (r) { return r.json(); }).then(function (gd) {
      var small = function () { return window.innerWidth < 720; };
      var g = new Graph(ac, gd, {
        ring: 560, cell: 30, r0: 1.9, rk: 0.78, gravity: 0.014, link: 70, spring: 0.0016, warm: 320, drift: 1.6, edgeAlpha: 0.07,
        pad: small() ? 30 : 84, aspect: small() ? 0.6 : 1.3, labelMax: 12, labelHits: 0, perCluster: true, regions: gd.clusters.map(function (c) { return c[2] || c[1]; }), regionsOnTop: small(),
        padL: function () { return small() ? 18 : panel.getBoundingClientRect().right - ac.getBoundingClientRect().left + 30; },
        padT: function () { return small() ? panel.getBoundingClientRect().bottom - ac.getBoundingClientRect().top + 36 : 70; },
        padB: small() ? 100 : 70,
        avoid: function () { var a = [rectOf(panel, 10), rectOf(zoomBox, 10)]; if (card.classList.contains("on")) a.push(rectOf(card, 10)); return a; },
        labels: function (rel) { return small() && rel < 1.35 ? 0 : Math.round(Math.min(70, (small() ? 4 : 12) + (rel - 1) * 26)); }
      });
      var bySlug = {}; g.nodes.forEach(function (n) { bySlug[n.slug] = n; });
      function show(n) {
        g.select(n);
        if (!n) { card.classList.remove("on"); try { history.replaceState(null, "", location.pathname); } catch (e) {} return; }
        card.setAttribute("data-c", gd.clusters[n.c][0]);
        var near = n.adj.map(function (k) { return g.nodes[k]; }).sort(function (a, b) { return b.deg - a.deg; }).slice(0, small() ? 0 : 4);
        var nearHtml = near.length ? "<ul>" + near.map(function (m) { return '<li><a href="#' + m.slug + '" data-go="' + m.slug + '">' + esc(m.title) + "</a></li>"; }).join("") + "</ul>" : "";
        card.innerHTML = '<button class="x" type="button" aria-label="閉じる">×</button><div class="mono"><i class="dot"></i>' + esc(gd.clusters[n.c][1]) + " · " + n.adj.length + ' 件の参照</div><h2>' + esc(n.title) + "</h2><p>" + esc(n.desc) + "</p>" + nearHtml + '<a class="go" href="' + ROOT + "concepts/" + n.slug + '/">記事を読む <span>→</span></a>';
        $$("[data-go]", card).forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); var m = bySlug[a.getAttribute("data-go")]; if (m) { show(m); focusOn(m); } }); });
        $(".x", card).addEventListener("click", function () { show(null); });
        card.classList.add("on");
        try { history.replaceState(null, "", "#" + n.slug); } catch (e) {}
      }
      function focusOn(n) {
        var sz = g.size(), pr = panel.getBoundingClientRect(), ar = ac.getBoundingClientRect();
        var ch = card.offsetHeight || 260;
        var box = small() ? [36, pr.bottom - ar.top + 44, sz[0] - 36, sz[1] - ch - 110] : [pr.right - ar.left + 120, 80, sz[0] - 460, sz[1] - 80];
        if (n.adj.length) g.frame(n, box); else g.center(n, 1.4, (box[0] + box[2]) / 2, (box[1] + box[3]) / 2);
      }
      var ptrs = {}, moved = 0, lastDist = 0;
      ac.addEventListener("pointerdown", function (e) { ac.setPointerCapture(e.pointerId); ptrs[e.pointerId] = [e.clientX, e.clientY]; moved = 0; ac.classList.add("drag"); });
      ac.addEventListener("pointermove", function (e) {
        var r = ac.getBoundingClientRect(), ids = Object.keys(ptrs);
        if (ptrs[e.pointerId]) {
          var p = ptrs[e.pointerId], dx = e.clientX - p[0], dy = e.clientY - p[1];
          if (ids.length === 1) { g.pan(dx, dy); moved += Math.abs(dx) + Math.abs(dy); }
          ptrs[e.pointerId] = [e.clientX, e.clientY];
          if (ids.length === 2) {
            var a = ptrs[ids[0]], b = ptrs[ids[1]], dist = Math.hypot(a[0] - b[0], a[1] - b[1]);
            if (lastDist) g.zoom(dist / lastDist, (a[0] + b[0]) / 2 - r.left, (a[1] + b[1]) / 2 - r.top);
            lastDist = dist; moved += 10;
          }
        } else {
          var n = g.pick(e.clientX - r.left, e.clientY - r.top); g.setHover(n); ac.style.cursor = n ? "pointer" : "";
        }
      });
      var up = function (e) {
        var r = ac.getBoundingClientRect();
        if (ptrs[e.pointerId] && moved < 6) show(g.pick(e.clientX - r.left, e.clientY - r.top));
        delete ptrs[e.pointerId]; lastDist = 0; if (!Object.keys(ptrs).length) ac.classList.remove("drag");
      };
      ac.addEventListener("pointerup", up); ac.addEventListener("pointercancel", up);
      ac.addEventListener("pointerleave", function () { g.setHover(null); });
      ac.addEventListener("wheel", function (e) { e.preventDefault(); var r = ac.getBoundingClientRect(); g.zoom(Math.exp(-e.deltaY * 0.0016), e.clientX - r.left, e.clientY - r.top); }, { passive: false });
      $$("[data-zoom]", atlas).forEach(function (b) { b.addEventListener("click", function () { var z = b.getAttribute("data-zoom"); if (z === "fit") g.fit(); else g.zoom(z === "in" ? 1.6 : 1 / 1.6); }); });
      $$(".legend button[data-c]", atlas).forEach(function (b, i) {
        b.addEventListener("click", function () { var on = b.getAttribute("aria-pressed") !== "true"; b.setAttribute("aria-pressed", on ? "true" : "false"); g.toggle(i, on); });
      });
      var shownEl = $(".atlas-shown", atlas), totalN = g.nodes.length, tOn = { 1: true, 2: true, 3: true };
      var tCount = { 1: 0, 2: 0, 3: 0 }; g.nodes.forEach(function (n) { tCount[n.tier] = (tCount[n.tier] || 0) + 1; });
      $$(".legend button[data-t]", atlas).forEach(function (b) {
        b.addEventListener("click", function () {
          var on = b.getAttribute("aria-pressed") !== "true", t = +b.getAttribute("data-t");
          b.setAttribute("aria-pressed", on ? "true" : "false"); g.toggleTier(t, on); tOn[t] = on;
          var n = 0; for (var k in tOn) if (tOn[k]) n += tCount[k] || 0;
          if (shownEl) shownEl.textContent = n === totalN ? "" : n.toLocaleString() + " / " + totalN.toLocaleString() + " 概念を表示";
        });
      });
      var h = decodeURIComponent(location.hash.slice(1));
      if (h && bySlug[h]) { show(bySlug[h]); focusOn(bySlug[h]); }
      atlas.classList.add("ready");
    });
  }
})();
