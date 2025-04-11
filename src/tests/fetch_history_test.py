import os
import unittest
from tkinter import Tk
from services.fetch_history import FetchHistory
from werkzeug.security import generate_password_hash
import csv

class TestFetchHistory(unittest.TestCase):
    def setUp(self):

        self.username = "username_test"

        self.history = FetchHistory(self, self.username)
    
    def test_fetch_history(self):

        result = self.history._fetch_history()
        self.assertEqual(result, [])