# -*- coding: utf-8 -*-
"""分野の属性を config/sources.yaml から引く共通処理。

物理の分野(research_domains で field: "physics" を持つもの)は、Tier 分類と記事生成で
別の基準・指示文を使う。分野の一覧をスクリプトごとに持たず、ここから引く。
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOURCES_PATH = os.path.join(BASE, "config", "sources.yaml")

# sources.yaml を読めないとき(yaml 未導入など)の控え。sources.yaml と揃えること。
_PHYSICS_FALLBACK = (
    "quantum_mechanics", "relativity", "cosmology_astrophysics", "particle_physics_qft",
    "string_theory", "statistical_physics", "condensed_matter",
    "mathematical_physics", "computational_physics",
)


def physics_domains():
    """物理の分野キーの集合を返す。"""
    try:
        import yaml
        with open(SOURCES_PATH, encoding="utf-8") as f:
            domains = (yaml.safe_load(f) or {}).get("research_domains") or {}
        found = {k for k, v in domains.items() if isinstance(v, dict) and v.get("field") == "physics"}
        return found or set(_PHYSICS_FALLBACK)
    except Exception:
        return set(_PHYSICS_FALLBACK)
