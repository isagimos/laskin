import os
import unittest
from tkinter import Tk
from repositories.users_repository import UsersRepository
from werkzeug.security import generate_password_hash
import csv

class TestLogin(unittest.TestCase):
    def setUp(self):

        self.login = UsersRepository(self)

        self.username = "username_test"
        self.password = "abcabcabc"
    
    def test_login(self):
        result = self.login.check_username_and_password(self.username, self.password)
        self.assertEqual(result, "Väärä käyttäjätunnus tai salasana")