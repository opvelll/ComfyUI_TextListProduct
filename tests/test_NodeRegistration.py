import unittest
import importlib
from pathlib import Path
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR.parent))
PLUGIN_INIT = importlib.import_module(ROOT_DIR.name)


class TestNodeRegistration(unittest.TestCase):
    def test_all_nodes_are_registered(self):
        expected_keys = {
            "TextListProduct",
            "TextListProductWithSingleA",
            "TextListProductWithSingleB",
            "TextListProductWithSingleBoth",
            "ProductedString",
            "PromptPairConcat",
        }
        self.assertEqual(set(PLUGIN_INIT.NODE_CLASS_MAPPINGS.keys()), expected_keys)
        self.assertEqual(
            set(PLUGIN_INIT.NODE_DISPLAY_NAME_MAPPINGS.keys()), expected_keys
        )

    def test_registered_nodes_expose_required_comfyui_attributes(self):
        for key, node_class in PLUGIN_INIT.NODE_CLASS_MAPPINGS.items():
            self.assertTrue(hasattr(node_class, "INPUT_TYPES"), key)
            self.assertTrue(hasattr(node_class, "RETURN_TYPES"), key)
            self.assertTrue(hasattr(node_class, "FUNCTION"), key)
            self.assertTrue(hasattr(node_class, "CATEGORY"), key)


if __name__ == "__main__":
    unittest.main()
