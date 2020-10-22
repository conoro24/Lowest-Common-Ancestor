import LCA2
import unittest

class TestLCA2(unittest.TestCase):

    def test_1(self):
        self.assertEqual(LCA2.lca(LCA2.root, 4, 5), 2)

    def test_2(self):
        self.assertEqual(LCA2.lca(LCA2.root, 3, 4), 1)

    def test_3(self):
        self.assertEqual(LCA2.lca(LCA2.root, 6, 8), 3)


if __name__ == '__main__':
    unittest.main()
