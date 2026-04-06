#!/usr/bin/env python3
"""核心論文（seed papers）のターゲット取得 — OpenAlex API"""
import httpx, os, re, time

OA = "https://api.openalex.org/works"
RAW = "/Users/yuta/workspace/projects/researcher/raw/papers"
ML = "researcher@example.com"

def slug(t):
    return re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', t.lower())).strip('-')[:80]

def inv2t(inv):
    if not inv: return ''
    wp = []
    for w, ps in inv.items():
        for p in ps:
            wp.append((p, w))
    wp.sort()
    return ' '.join(w for _, w in wp)

def fetch_save(query, domain):
    time.sleep(0.4)
    try:
        r = httpx.get(OA, params={
            'search': query, 'per_page': 1,
            'sort': 'cited_by_count:desc', 'mailto': ML
        }, timeout=30)
        if r.status_code != 200:
            return f'API {r.status_code}'
        results = r.json().get('results', [])
        if not results:
            return 'NO_RESULT'
        w = results[0]
        ti = (w.get('title') or '').replace('\n', ' ')
        ab = inv2t(w.get('abstract_inverted_index'))
        yr = w.get('publication_year', '')
        ci = w.get('cited_by_count', 0)
        aus = ', '.join(
            a.get('author', {}).get('display_name', '')
            for a in (w.get('authorships', []) or [])[:5]
        )
        sl = slug(ti)
        dd = os.path.join(RAW, domain)
        os.makedirs(dd, exist_ok=True)
        fp = os.path.join(dd, sl + '.md')
        if os.path.exists(fp):
            return f'EXISTS {ti[:40]} c:{ci}'
        with open(fp, 'w') as f:
            f.write(
                f'---\ntitle: "{ti}"\nauthors: "{aus}"\n'
                f'year: {yr}\ncitations: {ci}\n'
                f'domain: "{domain}"\nsource: "seed"\n---\n\n'
                f'# {ti}\n\n{aus} ({yr}) cited:{ci}\n\n'
                f'## Abstract\n\n{ab}\n'
            )
        return f'NEW {ti[:40]} c:{ci}'
    except Exception as e:
        return f'ERR: {e}'

seeds = [
    ('behavioral_economics', 'Thinking Fast and Slow Kahneman'),
    ('behavioral_economics', 'Nudge Improving Decisions Health Wealth Happiness'),
    ('behavioral_economics', 'bounded rationality Herbert Simon satisficing'),
    ('complexity_science', 'Thinking in Systems Donella Meadows primer'),
    ('complexity_science', 'Leverage points places intervene system Meadows'),
    ('cognitive_science', 'Cognition in the Wild Hutchins distributed'),
    ('cognitive_science', 'Dual-process theories higher cognition Evans Stanovich'),
    ('psychology', 'Flow psychology optimal experience Csikszentmihalyi'),
    ('psychology', 'Trust in automation human factors Lee See'),
    ('psychology', 'self-efficacy toward unifying theory behavioral change Bandura'),
    ('sociology', 'Rise of the Network Society Manuel Castells'),
    ('sociology', 'Reassembling the Social Latour actor-network'),
    ('economics', 'GPTs are GPTs labor market impact language models'),
    ('economics', 'Generative AI at work Brynjolfsson'),
    ('economics', 'Turing Trap dangers AI Brynjolfsson'),
    ('hci', 'Guidelines for Human-AI Interaction Amershi CHI'),
    ('hci', 'Human-Centered Artificial Intelligence Shneiderman'),
    ('hci', 'Principles mixed-initiative user interfaces Horvitz'),
    ('organization_science', 'knowledge-creating company Nonaka Takeuchi'),
    ('organization_science', 'evolutionary theory economic change Nelson Winter'),
    ('neuroscience', 'social brain hypothesis Dunbar neocortex group size'),
    ('neuroscience', 'Whatever next predictive brains situated agents Clark'),
    ('history_of_technology', 'Technological Revolutions Financial Capital Perez'),
    ('history_of_technology', 'Visible Hand managerial revolution Chandler'),
    ('ai_governance', 'global landscape AI ethics guidelines Jobin'),
    ('ai_governance', 'EU AI Act risk-based approach artificial intelligence'),
    ('systems_engineering', 'Safety-I Safety-II resilience Hollnagel'),
    ('systems_engineering', 'Engineering safer world systems thinking safety Leveson'),
    ('systems_engineering', 'risk management dynamic society Rasmussen'),
    ('philosophy', 'fourth revolution Floridi information ethics'),
    ('philosophy', 'consciousness explained Dennett'),
    ('philosophy', 'shared cooperative activity Bratman intentions'),
    ('anthropology', 'human-machine reconfigurations Suchman'),
    ('anthropology', 'Making anthropology archaeology art architecture Ingold'),
    ('evolutionary_biology', 'Not By Genes Alone cultural evolution Richerson Boyd'),
    ('evolutionary_biology', 'Selfish Gene Dawkins memes'),
]

new_count = 0
for domain, query in seeds:
    result = fetch_save(query, domain)
    if result.startswith('NEW'):
        new_count += 1
    print(f'[{domain}] {result}')

print(f'\nTotal new: {new_count} / {len(seeds)}')
