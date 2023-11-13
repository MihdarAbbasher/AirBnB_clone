"""Test base model module """
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = Place()
        self.assertIsInstance(s, (Place))

    def test_none(self):
        """test none func."""
        s = Place()
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
