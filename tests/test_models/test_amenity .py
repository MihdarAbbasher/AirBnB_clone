"""Test base model module """
import unittest
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = Amenity()
        self.assertIsInstance(s, (Amenity))

    def test_none(self):
        """test none func."""
        s = Amenity()
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
