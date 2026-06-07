#!/usr/bin/env python3
"""
Cross-reference suggestion tool for wiki concepts based on shared mechanisms.

Analyzes mechanism overlap between concepts and suggests/applies cross-reference
improvements to wiki articles.
"""

import json
import os
import math
import argparse
import re
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict

BASE = "/Users/yuta/workspace/projects/researcher"
CONCEPTS_JSON = os.path.join(BASE, "wiki/_meta/concepts.json")
GRAPH_JSON = os.path.join(BASE, "wiki/_meta/concepts-graph.json")
WIKI_DIR = os.path.join(BASE, "wiki/concepts")


class ConceptLinker:
    def __init__(self):
        self.concepts = {}  # type: Dict[str, Dict]
        self.graph_edges = set()  # type: Set[Tuple[str, str]]
        self.mechanism_to_concepts = defaultdict(set)  # type: Dict[str, Set[str]]
        self.mechanism_counts = {}  # type: Dict[str, int]

    def load_data(self):
        """Load concepts.json and concepts-graph.json."""
        # Load concepts metadata
        with open(CONCEPTS_JSON, 'r', encoding='utf-8') as f:
            concepts_data = json.load(f)

        # Filter to only concepts with wiki articles
        # concepts.json is a list of concept objects
        for concept in concepts_data:
            slug = concept.get('slug')
            if not slug:
                continue

            article_path = os.path.join(WIKI_DIR, f"{slug}.md")
            if os.path.exists(article_path):
                self.concepts[slug] = concept

                # Build mechanism index
                mechanisms = concept.get('mechanisms', [])
                for mechanism in mechanisms:
                    self.mechanism_to_concepts[mechanism].add(slug)

        # Calculate mechanism counts
        for mechanism, concept_set in self.mechanism_to_concepts.items():
            self.mechanism_counts[mechanism] = len(concept_set)

        # Load graph edges
        with open(GRAPH_JSON, 'r', encoding='utf-8') as f:
            graph_data = json.load(f)

        for edge in graph_data.get('edges', []):
            source = edge.get('source')
            target = edge.get('target')
            if source and target:
                # Store bidirectional edges as normalized pairs
                pair = tuple(sorted([source, target]))
                self.graph_edges.add(pair)

    def calculate_score(self, shared_mechanisms):
        # type: (List[str]) -> float
        """
        Calculate match quality score based on shared mechanisms.

        Formula: sum of 1 / log2(N + 1) for each shared mechanism,
        where N is the number of concepts having that mechanism.
        """
        score = 0.0
        for mechanism in shared_mechanisms:
            n = self.mechanism_counts.get(mechanism, 1)
            score += 1.0 / math.log2(n + 1)
        return score

    def find_suggestions(self, target_slug=None):
        # type: (Optional[str]) -> List[Dict]
        """
        Find cross-reference suggestions.

        Args:
            target_slug: If provided, only find suggestions for this concept

        Returns:
            List of suggestions sorted by score (descending)
        """
        suggestions = []

        # Determine which concepts to process
        if target_slug:
            if target_slug not in self.concepts:
                print(f"Warning: concept '{target_slug}' not found or has no wiki article")
                return []
            slugs_to_process = [target_slug]
        else:
            slugs_to_process = list(self.concepts.keys())

        # For each concept
        for slug_a in slugs_to_process:
            mechanisms_a = set(self.concepts[slug_a].get('mechanisms', []))

            # Compare with all other concepts
            for slug_b in self.concepts.keys():
                if slug_a >= slug_b:  # Skip self and avoid duplicates
                    continue

                # Check if already linked
                pair = tuple(sorted([slug_a, slug_b]))
                if pair in self.graph_edges:
                    continue

                # Find shared mechanisms
                mechanisms_b = set(self.concepts[slug_b].get('mechanisms', []))
                shared = mechanisms_a & mechanisms_b

                # Filter: need 2+ shared mechanisms
                if len(shared) < 2:
                    continue

                # Calculate score
                score = self.calculate_score(list(shared))

                suggestions.append({
                    'slug_a': slug_a,
                    'slug_b': slug_b,
                    'title_a': self.concepts[slug_a].get('title_ja', slug_a),
                    'title_b': self.concepts[slug_b].get('title_ja', slug_b),
                    'shared_mechanisms': sorted(list(shared)),
                    'shared_count': len(shared),
                    'score': score
                })

        # Sort by score descending
        suggestions.sort(key=lambda x: x['score'], reverse=True)
        return suggestions

    def print_suggestions(self, suggestions, count=50):
        # type: (List[Dict], int) -> None
        """Print suggestions in formatted output."""
        print("# Cross-Reference Suggestions\n")

        if not suggestions:
            print("No suggestions found.\n")
            return

        for i, sugg in enumerate(suggestions[:count], 1):
            print(f"## {i}. {sugg['slug_a']} ↔ {sugg['slug_b']} "
                  f"(score: {sugg['score']:.2f}, shared: {sugg['shared_count']})")
            print(f"   {sugg['title_a']} ↔ {sugg['title_b']}")
            print(f"   Shared mechanisms: {', '.join(sugg['shared_mechanisms'])}")
            print()

    def add_link_to_article(self, article_path, target_slug):
        # type: (str, str) -> bool
        """
        Add a link to the related concepts section of an article.

        Returns:
            True if link was added, False if already exists or section not found
        """
        with open(article_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Check if link already exists
        link_pattern = r'\[\[' + re.escape(target_slug) + r'\]\]'
        for line in lines:
            if re.search(link_pattern, line):
                return False  # Already exists

        # Find the "関連コンセプト" or "関連概念" section
        section_idx = None
        for i, line in enumerate(lines):
            if re.match(r'^##\s+関連', line):
                section_idx = i
                break

        if section_idx is None:
            return False  # Section not found

        # Find where to insert (after section header, before next section or end)
        insert_idx = section_idx + 1

        # Skip empty lines after header
        while insert_idx < len(lines) and lines[insert_idx].strip() == '':
            insert_idx += 1

        # Detect bullet style from existing items (prefer * over -)
        bullet_style = '*'
        if insert_idx < len(lines):
            first_item = lines[insert_idx].lstrip()
            if first_item.startswith('- '):
                bullet_style = '-'

        # Insert the new link
        new_link = f"{bullet_style}   [[{target_slug}]]\n"
        lines.insert(insert_idx, new_link)

        # Write back
        with open(article_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        return True

    def apply_suggestions(self, suggestions, count=50):
        # type: (List[Dict], int) -> None
        """
        Apply suggestions by editing wiki article files.

        For each suggested link pair (A, B), add B to A's related section
        and vice versa if both have articles.
        """
        applied_count = 0
        skipped_count = 0

        print("Applying cross-reference suggestions...\n")

        for i, sugg in enumerate(suggestions[:count], 1):
            slug_a = sugg['slug_a']
            slug_b = sugg['slug_b']

            article_a = os.path.join(WIKI_DIR, f"{slug_a}.md")
            article_b = os.path.join(WIKI_DIR, f"{slug_b}.md")

            # Check if both articles exist
            if not os.path.exists(article_a) or not os.path.exists(article_b):
                skipped_count += 1
                continue

            # Add bidirectional links
            added_a = self.add_link_to_article(article_a, slug_b)
            added_b = self.add_link_to_article(article_b, slug_a)

            if added_a or added_b:
                applied_count += 1
                print(f"{i}. Applied: {slug_a} ↔ {slug_b} (score: {sugg['score']:.2f})")
                if added_a:
                    print(f"   Added [[{slug_b}]] to {slug_a}")
                if added_b:
                    print(f"   Added [[{slug_a}]] to {slug_b}")
            else:
                skipped_count += 1
                print(f"{i}. Skipped: {slug_a} ↔ {slug_b} (links already exist or section not found)")

        print(f"\nSummary: {applied_count} pairs modified, {skipped_count} skipped")

    def print_stats(self):
        """Print statistics about mechanisms and connectivity."""
        print("# Mechanism Statistics\n")

        # Total concepts
        print(f"Total concepts with articles: {len(self.concepts)}")
        print(f"Total unique mechanisms: {len(self.mechanism_counts)}")
        print(f"Existing graph edges: {len(self.graph_edges)}")
        print()

        # Mechanism distribution
        print("## Mechanism Distribution\n")
        mechanism_list = sorted(
            self.mechanism_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print("Top 20 most common mechanisms:")
        for mechanism, count in mechanism_list[:20]:
            print(f"  {mechanism}: {count} concepts")
        print()

        print("Top 20 rarest mechanisms:")
        for mechanism, count in mechanism_list[-20:]:
            print(f"  {mechanism}: {count} concepts")
        print()

        # Concepts by mechanism count
        mech_per_concept = [len(c.get('mechanisms', [])) for c in self.concepts.values()]
        if mech_per_concept:
            avg_mech = sum(mech_per_concept) / len(mech_per_concept)
            print(f"Average mechanisms per concept: {avg_mech:.2f}")
            print(f"Max mechanisms in a concept: {max(mech_per_concept)}")
            print(f"Min mechanisms in a concept: {min(mech_per_concept)}")
        print()

        # Potential improvements
        suggestions = self.find_suggestions()
        print(f"## Connectivity Improvement Potential\n")
        print(f"Concepts with 2+ shared mechanisms not currently linked: {len(suggestions)}")
        if suggestions:
            print(f"Average score of top 50 suggestions: {sum(s['score'] for s in suggestions[:50]) / min(50, len(suggestions)):.2f}")


def main():
    parser = argparse.ArgumentParser(
        description='Analyze and suggest cross-references between wiki concepts based on shared mechanisms.'
    )
    parser.add_argument(
        '--count',
        type=int,
        default=50,
        help='Number of suggestions to show/apply (default: 50)'
    )
    parser.add_argument(
        '--concept',
        type=str,
        help='Show suggestions only for a specific concept (by slug)'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply the suggestions by editing wiki article files'
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show statistics about mechanisms and connectivity'
    )

    args = parser.parse_args()

    # Initialize and load data
    linker = ConceptLinker()
    linker.load_data()

    # Execute requested action
    if args.stats:
        linker.print_stats()
    else:
        suggestions = linker.find_suggestions(target_slug=args.concept)

        if args.apply:
            linker.apply_suggestions(suggestions, count=args.count)
        else:
            linker.print_suggestions(suggestions, count=args.count)


if __name__ == '__main__':
    main()
