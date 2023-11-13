"""Test base model module """
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """test base model class"""
    def test_init(self):
        """test init func."""
        s = State()
        self.assertIsInstance(s, (State))

    def test_none(self):
        """test none func."""
        s = State()
        s.name = "newName"
        self.assertEqual(s.name, "newName")


if __name__ == '__main__':
    unittest.main()
