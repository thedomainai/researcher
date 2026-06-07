#!/usr/bin/env python3
"""
Normalize mechanism names in wiki/_meta/concepts.json

Applies 5 normalization rules to standardize mechanism naming:
  1. Canonical mappings (synonym resolution)
  2. Domain-prefix stripping (preserves structural prefixes)
  3. Compound mechanism splitting (on "と")
  4. Result-suffix stripping (の解消, の削減, etc.)
  5. Deduplication within each concept

Usage:
    python3 tools/normalize_mechanisms.py              # Dry run (show changes)
    python3 tools/normalize_mechanisms.py --apply      # Apply changes
    python3 tools/normalize_mechanisms.py --stats      # Before/after statistics

Examples:
    "限定合理性" → "有限合理性" (Rule 1)
    "取引コストの削減" → "取引コスト" (Rule 1 & 4)
    "組織ルーチンの経路依存性" → "経路依存性" (Rule 2)
    "情報の非対称性と認知バイアス" → ["情報の非対称性", "認知バイアス"] (Rule 3)

Preserves structural variants:
    "正のフィードバックループ" → kept as is (structural)
    "自律的フィードバックループ" → kept as is (structural)

Safety:
    - Creates backup at wiki/_meta/concepts.json.backup before applying
    - Dry run shows all changes before applying
    - All other fields in concepts.json are preserved unchanged
"""

import json
import sys
import shutil
from typing import List, Dict, Set, Tuple, Optional
from collections import defaultdict

BASE = "/Users/yuta/workspace/projects/researcher"
CONCEPTS_PATH = f"{BASE}/wiki/_meta/concepts.json"
BACKUP_PATH = f"{CONCEPTS_PATH}.backup"

# Rule 1: Exact canonical mappings (synonym resolution)
CANONICAL_MAP = {
    "限定合理性": "有限合理性",
    "シグナリング効果": "シグナリング",
    "取引コストの削減": "取引コスト",
    "取引コストの最小化": "取引コスト",
    "取引コスト削減": "取引コスト",
    "情報の非対称性の解消": "情報の非対称性",
    "情報の非対称性の低減": "情報の非対称性",
    "情報の非対称性の緩和": "情報の非対称性",
    "情報非対称性": "情報の非対称性",
    "情報非対称性の非開示的解消": "情報の非対称性",
    "価値の共創": "価値共創",
    "信頼のキャリブレーション": "信頼キャリブレーション",
    "オートメーション・バイアス": "自動化バイアス",
    "認知負荷の低減": "認知負荷",
    "認知負荷の最小化": "認知負荷",
}

# Rule 2: Core mechanisms for domain-prefix stripping
CORE_MECHANISMS = {
    "経路依存性",
    "フィードバックループ",
    "情報の非対称性",
    "エージェンシー問題",
    "インセンティブ設計",
}

# Structural prefixes that should NOT be stripped (without the connector)
STRUCTURAL_PREFIXES = {
    "自律的",
    "再帰的",
    "正",
    "負",
    "動的",
    "適応的",
    "正負",  # combined
}

# Rule 4: Result suffixes to strip
RESULT_SUFFIXES = [
    "の解消",
    "の削減",
    "の低減",
    "の緩和",
    "の最適化",
    "の最小化",
]


class MechanismNormalizer:
    def __init__(self):
        self.changes = defaultdict(list)
        self.known_mechanisms = set()

    def load_concepts(self) -> List[Dict]:
        """Load concepts.json"""
        with open(CONCEPTS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_concepts(self, concepts: List[Dict]) -> None:
        """Save concepts.json with backup"""
        shutil.copy2(CONCEPTS_PATH, BACKUP_PATH)
        with open(CONCEPTS_PATH, 'w', encoding='utf-8') as f:
            json.dump(concepts, f, ensure_ascii=False, indent=2)
        print(f"Backup saved to: {BACKUP_PATH}")
        print(f"Updated: {CONCEPTS_PATH}")

    def build_known_mechanisms(self, concepts: List[Dict]) -> None:
        """Build set of all known mechanisms for Rule 4"""
        for concept in concepts:
            for mech in concept.get('mechanisms', []):
                self.known_mechanisms.add(mech)
        # Add canonical targets
        self.known_mechanisms.update(CANONICAL_MAP.values())
        # Add core mechanisms
        self.known_mechanisms.update(CORE_MECHANISMS)

    def apply_rule1_canonical(self, mech: str) -> Tuple[str, Optional[str]]:
        """Rule 1: Exact canonical mapping"""
        if mech in CANONICAL_MAP:
            return CANONICAL_MAP[mech], "Rule 1: canonical"
        return mech, None

    def apply_rule2_domain_prefix(self, mech: str) -> Tuple[str, Optional[str]]:
        """Rule 2: Domain-prefix stripping"""
        for core in CORE_MECHANISMS:
            if mech.endswith(core) and mech != core:
                # Check if there's a "の" or "における" before core
                prefix_patterns = [
                    (f"の{core}", "の"),
                    (f"における{core}", "における")
                ]
                for pattern, connector in prefix_patterns:
                    if mech.endswith(pattern):
                        prefix = mech[:-len(pattern)]
                        # Don't strip if prefix is a structural modifier
                        if prefix not in STRUCTURAL_PREFIXES:
                            return core, "Rule 2: domain-prefix"
                        else:
                            # Structural prefix detected, keep as is
                            return mech, None
        return mech, None

    def apply_rule3_compound_split(self, mech: str) -> Tuple[List[str], Optional[str]]:
        """Rule 3: Compound mechanism splitting.

        Only split when BOTH parts are already known mechanisms in the corpus.
        This prevents breaking meaningful compound expressions.
        """
        if "と" not in mech:
            return [mech], None

        # Try splitting at each "と" position (only first occurrence)
        idx = mech.find("と")
        while idx > 0:
            left = mech[:idx].strip()
            right = mech[idx + 1:].strip()

            # Both parts must be known mechanisms and >= 3 chars
            if (len(left) >= 3 and len(right) >= 3
                    and left in self.known_mechanisms
                    and right in self.known_mechanisms):
                return [left, right], "Rule 3: split"

            # Also check after applying canonical mapping
            left_canon = CANONICAL_MAP.get(left, left)
            right_canon = CANONICAL_MAP.get(right, right)
            if (left_canon in self.known_mechanisms
                    and right_canon in self.known_mechanisms
                    and (left_canon != left or right_canon != right)):
                return [left_canon, right_canon], "Rule 3: split"

            # Try next "と"
            idx = mech.find("と", idx + 1)

        return [mech], None

    def apply_rule4_result_suffix(self, mech: str) -> Tuple[str, Optional[str]]:
        """Rule 4: Result-suffix stripping"""
        for suffix in RESULT_SUFFIXES:
            if mech.endswith(suffix):
                base = mech[:-len(suffix)]
                # Only strip if:
                # - Base is >= 3 characters
                # - Base is a known mechanism or in canonical map
                if len(base) >= 3 and (base in self.known_mechanisms or base in CANONICAL_MAP):
                    return base, "Rule 4: result-suffix"
        return mech, None

    def normalize_mechanism(self, mech: str, slug: str) -> List[Tuple[str, str, Optional[str]]]:
        """
        Normalize a single mechanism through all rules.
        Returns list of (original, normalized, reason) tuples.
        """
        results = []
        current = mech
        reason_chain = []

        # Rule 1: Canonical mapping
        normalized, reason = self.apply_rule1_canonical(current)
        if reason:
            reason_chain.append(reason)
            results.append((current, normalized, reason))
            current = normalized

        # Rule 2: Domain-prefix stripping
        normalized, reason = self.apply_rule2_domain_prefix(current)
        if reason:
            reason_chain.append(reason)
            results.append((current, normalized, reason))
            current = normalized

        # Rule 3: Compound splitting (returns list)
        parts, reason = self.apply_rule3_compound_split(current)
        if reason:
            reason_chain.append(reason)
            # If split happened, record it and process each part separately
            if len(parts) > 1:
                # Recursively normalize each part (but avoid infinite recursion)
                final_parts = []
                for part in parts:
                    # Apply only Rule 1 and Rule 4 to parts
                    p = part
                    p, r1 = self.apply_rule1_canonical(p)
                    p, r2 = self.apply_rule4_result_suffix(p)
                    final_parts.append(p)
                # Return with a special marker for split
                display = ' + '.join(f'"{p}"' for p in final_parts)
                return [(mech, f"SPLIT:{json.dumps(final_parts, ensure_ascii=False)}", f"Rule 3: split → {display}")]

        # Rule 4: Result-suffix stripping
        normalized, reason = self.apply_rule4_result_suffix(current)
        if reason:
            reason_chain.append(reason)
            results.append((current, normalized, reason))
            current = normalized

        # If any change was made, return the final result
        if results:
            return [(mech, current, " → ".join(reason_chain))]

        return []

    def normalize_concept(self, concept: Dict) -> Dict:
        """Normalize all mechanisms in a concept"""
        slug = concept['slug']
        mechanisms = concept.get('mechanisms', [])

        if not mechanisms:
            return concept

        new_mechanisms = []

        for mech in mechanisms:
            changes = self.normalize_mechanism(mech, slug)

            if changes:
                # Record changes for reporting
                for orig, norm, reason in changes:
                    self.changes[slug].append((orig, norm, reason))

                # Handle split mechanisms
                final = changes[-1][1]
                if final.startswith('SPLIT:'):
                    # Parse the JSON list
                    parts = json.loads(final[6:])
                    new_mechanisms.extend(parts)
                else:
                    new_mechanisms.append(final)
            else:
                new_mechanisms.append(mech)

        # Rule 5: Deduplication
        original_count = len(new_mechanisms)
        new_mechanisms = list(dict.fromkeys(new_mechanisms))  # Preserve order

        if len(new_mechanisms) < original_count:
            dup_count = original_count - len(new_mechanisms)
            self.changes[slug].append(
                (f"{dup_count} duplicates", "removed", "Rule 5: dedup")
            )

        concept['mechanisms'] = new_mechanisms
        return concept

    def normalize_all(self, concepts: List[Dict]) -> List[Dict]:
        """Normalize all concepts"""
        # First pass: build known mechanisms set
        self.build_known_mechanisms(concepts)

        # Second pass: normalize
        normalized = []
        for concept in concepts:
            normalized.append(self.normalize_concept(concept))

        return normalized

    def print_changes(self) -> None:
        """Print changes in dry-run format"""
        if not self.changes:
            print("No changes needed.")
            return

        print("# Mechanism Normalization (Dry Run)\n")
        print("## Changes\n")

        for slug in sorted(self.changes.keys()):
            print(f"{slug}:")
            for orig, norm, reason in self.changes[slug]:
                print(f'  - "{orig}" → "{norm}" ({reason})')
            print()

        # Summary
        total_concepts = len(self.changes)
        total_changes = sum(len(changes) for changes in self.changes.values())
        print("## Summary")
        print(f"Total concepts affected: {total_concepts}")
        print(f"Total mechanism changes: {total_changes}")

    def print_stats(self, before: List[Dict], after: List[Dict]) -> None:
        """Print before/after statistics"""
        before_mechs = [m for c in before for m in c.get('mechanisms', [])]
        after_mechs = [m for c in after for m in c.get('mechanisms', [])]

        print("## Statistics\n")
        print(f"Total concepts: {len(before)}")
        print(f"Concepts affected: {len(self.changes)}")
        total_changes = sum(len(changes) for changes in self.changes.values())
        print(f"Total mechanism changes: {total_changes}")
        print(f"\nTotal mechanisms before: {len(before_mechs)}")
        print(f"Total mechanisms after: {len(after_mechs)}")
        print(f"  (increase due to compound splitting)")
        print(f"\nUnique mechanisms before: {len(set(before_mechs))}")
        print(f"Unique mechanisms after: {len(set(after_mechs))}")

        change = len(set(after_mechs)) - len(set(before_mechs))
        if change > 0:
            print(f"Unique mechanism change: +{change} (compound splits)")
        elif change < 0:
            print(f"Unique mechanism reduction: {-change}")
        else:
            print("Unique mechanism change: 0")


def main():
    args = sys.argv[1:]
    apply_changes = '--apply' in args
    show_stats = '--stats' in args

    normalizer = MechanismNormalizer()

    # Load concepts
    concepts = normalizer.load_concepts()

    # Deep copy for comparison
    import copy
    original_concepts = copy.deepcopy(concepts)

    # Normalize
    normalized_concepts = normalizer.normalize_all(concepts)

    if show_stats:
        normalizer.print_stats(original_concepts, normalized_concepts)
    else:
        normalizer.print_changes()

    if apply_changes:
        print("\n" + "="*60)
        print("APPLYING CHANGES")
        print("="*60 + "\n")
        normalizer.save_concepts(normalized_concepts)
        print("\nDone!")
    elif not show_stats:
        print("\n(Dry run - use --apply to save changes)")


if __name__ == '__main__':
    main()
