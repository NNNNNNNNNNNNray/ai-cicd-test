import os
import sys
import unittest


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


from ai_cicd_test.core import add  # noqa: E402


class TestCore(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(1, 2), 2)
        self.assertEqual(add(3, 4), 12)
        self.assertEqual(add(0, 999), 0)


if __name__ == "__main__":
    unittest.main()

