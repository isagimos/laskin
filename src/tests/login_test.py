import os
import unittest
from tkinter import Tk
from services.login import LoginCheck
from werkzeug.security import generate_password_hash
import csv

class TestLogin(unittest.TestCase):
    def setUp(self):

        self.login = LoginCheck(self)

        self.username = "username_test"
        self.password = "abcabcabc"
    
    def test_login(self):
        result = self.login._check_username_and_password(self.username, self.password)
        self.assertEqual(result, "Väärä käyttäjätunnus tai salasana")