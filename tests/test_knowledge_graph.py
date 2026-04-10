import json
import os
import tempfile
import unittest

from tools.lib.knowledge_graph import build_knowledge_graph, write_graph_artifacts


class KnowledgeGraphTests(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.base = self.tmpdir.name
        self.wiki_concepts = os.path.join(self.base, "wiki", "concepts")
        self.wiki_meta = os.path.join(self.base, "wiki", "_meta")
        self.raw_demo = os.path.join(self.base, "raw", "papers", "demo")
        os.makedirs(self.wiki_concepts, exist_ok=True)
        os.makedirs(self.wiki_meta, exist_ok=True)
        os.makedirs(self.raw_demo, exist_ok=True)

        with open(os.path.join(self.raw_demo, "source.md"), "w", encoding="utf-8") as handle:
            handle.write("# Source\n")

        concepts = [
            {
                "slug": "alpha-concept",
                "title_ja": "Alpha Concept",
                "title_en": "Alpha Concept",
                "tier": 1,
                "description": "alpha",
                "related_domains": ["demo"],
                "key_sources": ["Alpha Source"],
            },
            {
                "slug": "beta-node",
                "title_ja": "Beta Concept",
                "title_en": "Beta Concept",
                "tier": 2,
                "description": "beta",
                "related_domains": ["demo"],
                "key_sources": ["Beta Source"],
            },
            {
                "slug": "gamma-node",
                "title_ja": "ガンマ概念",
                "title_en": "Gamma Concept",
                "tier": 3,
                "description": "gamma",
                "related_domains": ["demo"],
                "key_sources": ["Gamma Source"],
            },
        ]
        with open(os.path.join(self.wiki_meta, "concepts.json"), "w", encoding="utf-8") as handle:
            json.dump(concepts, handle, ensure_ascii=False, indent=2)

        with open(os.path.join(self.wiki_concepts, "alpha-concept.md"), "w", encoding="utf-8") as handle:
            handle.write(
                "# Alpha Concept\n\n"
                "## Related Concepts\n"
                "- [[beta-node]]\n"
                "- [[ガンマ概念（Gamma Concept）]]\n"
                "- [[Missing Concept]]\n"
                "- [[beta-node|Beta]]\n\n"
                "## Sources\n"
                "- raw/papers/demo/source.md\n"
                "- raw/papers/demo/missing.md\n"
            )

        with open(os.path.join(self.wiki_concepts, "beta-node.md"), "w", encoding="utf-8") as handle:
            handle.write(
                "# Beta Concept\n\n"
                "## Related Concepts\n"
                "- [[alpha-concept]]\n"
            )

        with open(os.path.join(self.wiki_concepts, "gamma-node.md"), "w", encoding="utf-8") as handle:
            handle.write("# ガンマ概念\n")

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_build_knowledge_graph_resolves_aliases_and_unresolved_targets(self):
        graph, backlinks = build_knowledge_graph(base_dir=self.base)

        summary = graph["summary"]
        self.assertEqual(summary["resolved_nodes"], 3)
        self.assertEqual(summary["unresolved_nodes"], 1)
        self.assertEqual(summary["edges"], 4)
        self.assertEqual(summary["link_mentions"], 5)
        self.assertEqual(summary["valid_source_refs"], 1)
        self.assertEqual(summary["invalid_source_refs"], 1)

        edge_map = {(edge["source"], edge["target"]): edge for edge in graph["edges"]}
        self.assertIn(("alpha-concept", "beta-node"), edge_map)
        self.assertEqual(edge_map[("alpha-concept", "beta-node")]["weight"], 2)
        self.assertEqual(edge_map[("alpha-concept", "gamma-node")]["mentions"][0]["resolved_via"], "alias")

        unresolved_nodes = [node for node in graph["nodes"] if not node["resolved"]]
        self.assertEqual(len(unresolved_nodes), 1)
        self.assertEqual(unresolved_nodes[0]["label"], "Missing Concept")

        beta_backlinks = backlinks["nodes"]["beta-node"]["inbound"]
        self.assertEqual(len(beta_backlinks), 1)
        self.assertEqual(beta_backlinks[0]["id"], "alpha-concept")

        unresolved = graph["unresolved_mentions"]
        self.assertEqual(len(unresolved), 1)
        self.assertEqual(unresolved[0]["raw_target"], "Missing Concept")

    def test_write_graph_artifacts_creates_expected_files(self):
        write_graph_artifacts(base_dir=self.base)

        graph_path = os.path.join(self.wiki_meta, "concepts-graph.json")
        backlinks_path = os.path.join(self.wiki_meta, "backlinks.json")
        self.assertTrue(os.path.exists(graph_path))
        self.assertTrue(os.path.exists(backlinks_path))

        with open(graph_path, encoding="utf-8") as handle:
            graph = json.load(handle)
        with open(backlinks_path, encoding="utf-8") as handle:
            backlinks = json.load(handle)
        self.assertEqual(graph["summary"]["resolved_nodes"], 3)
        self.assertIn("beta-node", backlinks["nodes"])


if __name__ == "__main__":
    unittest.main()
