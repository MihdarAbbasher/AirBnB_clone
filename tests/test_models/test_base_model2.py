"""Test base model module """
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test base model class"""

    def test_init(self):
        """test init func."""
        s = BaseModel()
        self.assertIsInstance(s, (BaseModel))

    def test_none(self):
        """test none func."""
        s = BaseModel()
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
