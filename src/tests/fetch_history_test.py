import unittest
from services.fetch_history import FetchHistory

class TestHistory(unittest.TestCase):
    def setUp(self):
        self.username = "test_username"
        self.calculator = FetchHistory(self.username)
    
    def test_method_returns_list_of_calculations(self):
        history = self.calculator._fetch_history()
        print(history)
        self.assertEqual(history, "23")