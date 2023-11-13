"""Test base model module """
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = City()
        self.assertIsInstance(s, (City))

    def test_none(self):
        """test none func."""
        s = City()
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
