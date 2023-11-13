"""Test base model module """
import unittest
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = FileStorage()
        self.assertIsInstance(s, (FileStorage))


if __name__ == '__main__':
    unittest.main()
