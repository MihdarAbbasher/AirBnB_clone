"""Test base model module """
import unittest
from models import base_model


BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = base_model.BaseModel
        self.assertEqual(s, (BaseModel))

    def test_none(self):
        """test none func."""
        s = base_model.BaseModel
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
