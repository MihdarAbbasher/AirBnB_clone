"""Test base model module """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = User()
        self.assertIsInstance(s, (User))

    def test_none(self):
        """test none func."""
        s = User()
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
