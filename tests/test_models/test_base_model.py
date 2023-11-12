"""Test base model module """
import unittest
from models import base_model


class TestBaseModel(unittest.TestCase):

    """test base model class"""
    def test_init(self):
        """test init func."""
        s = base_model.BaseModel()
        self.assertEqual(type(s), "BaseModel")


if __name__ == '__main__':
    unittest.main()
