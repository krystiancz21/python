import unittest

def sort_desc(lista):
    """Sorts the list in descending order."""
    return sorted(lista, reverse=True)

class TestSortDesc(unittest.TestCase):
    def test_normal_list(self):
        """Tests sorting of a regular list of numbers."""
        self.assertEqual(sort_desc([3, 1, 4, 2]), [4, 3, 2, 1])
    
    def test_empty_list(self):
        """Tests sorting of an empty list."""
        self.assertEqual(sort_desc([]), [])
    
    def test_single_element(self):
        """Tests sorting of a single-element list."""
        self.assertEqual(sort_desc([1]), [1])

if __name__ == "__main__":
    unittest.main()
