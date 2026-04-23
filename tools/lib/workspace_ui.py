"""Shared workspace UI helpers for generated HTML views."""

from html import escape


NAV_ITEMS = (
    (
        "atlas",
        "Knowledge Atlas",
        "Graph topology and gap audit",
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="7" r="2.6"/><circle cx="18" cy="6" r="2.6"/><circle cx="12" cy="18" r="2.6"/><path d="M8.3 8.4l7 -1.8M7.6 9.2l3.2 6.4M16.7 8.2l-3.3 7"/></svg>',
    ),
    (
        "reader",
        "Article Reader",
        "Concept articles with backlinks",
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4.5h10.5a3 3 0 0 1 3 3V19H8a3 3 0 0 0-3 3z"/><path d="M8 4.5v17.5"/><path d="M11 8h5"/><path d="M11 11.5h5"/><path d="M11 15h4"/></svg>',
    ),
    (
        "index",
        "Wiki Index",
        "Tiered catalog and overview",
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 5h10"/><path d="M7 9.5h10"/><path d="M7 14h10"/><path d="M7 18.5h10"/><path d="M4 5h.01"/><path d="M4 9.5h.01"/><path d="M4 14h.01"/><path d="M4 18.5h.01"/></svg>',
    ),
)


def render_workspace_sidebar(active_view, summary_text, links):
    nav_html = []
    for key, title, subtitle, icon in NAV_ITEMS:
        href = escape(links[key], quote=True)
        class_name = "page-link active" if key == active_view else "page-link"
        aria = ' aria-current="page"' if key == active_view else ""
        nav_html.append(
            f'''<a class="{class_name}" href="{href}"{aria}>
        <span class="page-icon">{icon}</span>
        <span class="page-copy"><strong>{escape(title)}</strong><span>{escape(subtitle)}</span></span>
      </a>'''
        )

    return (
        '<aside class="page-rail">'
        '<div class="page-rail-card">'
        '<div class="page-rail-head">'
        '<span class="page-rail-eyebrow">Views</span>'
        '<span class="page-rail-badge">3 views</span>'
        '</div>'
        '<nav class="page-nav">'
        + "".join(nav_html)
        + '</nav>'
        '<div class="page-meta">'
        '<strong>Corpus snapshot</strong>'
        f'<span>{escape(summary_text)}</span>'
        '</div>'
        '</div>'
        '</aside>'
    )
