"""Test base model module """
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = Review()
        self.assertIsInstance(s, (Review))

    def test_none(self):
        """test none func."""
        s = Review()
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
