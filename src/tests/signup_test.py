import os
import unittest
from tkinter import Tk
from services.signup import SignUp
from werkzeug.security import generate_password_hash
import csv

class TestSignup(unittest.TestCase):
    def setUp(self):

        self.signup = SignUp(self)

        self.username = "test_username"
        self.username2 = "a"

        self.password1 = "abcabcabc"
        self.password2 = "abcabcabc"
        self.password3 = "123123123"

    def test_signup_different_passwords(self):
        result = self.signup._create_account(self.username, self.password1, self.password3)
        self.assertEqual(result, "Salasanat eivät täsmää")

    def test_signup_username_is_not_unique(self):
        # Create a test account and test if method returns False
        # Then remove the test account from users.csv
        file_path = os.path.join("data", "users.csv")
        with open(file_path, "a", encoding="utf-8") as f:
            new_test_user = f"{self.username};{generate_password_hash(self.password1)}"
            f.write(new_test_user + "\n")
        
        result = self.signup._create_account(self.username, self.password1, self.password2)

        with open(file_path, "r", encoding="utf-8") as f:
            users = f.readlines()
            users.pop()
        with open(file_path, "w", encoding="utf-8") as f:
            for user in users:
                f.write(user)

        self.assertEqual(result, "Tunnus on jo käytössä")

    def test_signup_account_created_successfully(self):
        result = self.signup._create_account(self.username, self.password1, self.password2)
        
        file_path = os.path.join("data", "users.csv")
        with open(file_path, "r", encoding="utf-8") as f:
            users = f.readlines()
            users.pop()
        with open(file_path, "w", encoding="utf-8") as f:
            for user in users:
                f.write(user)
        
        self.assertEqual(result, "Tunnus luotu")
    
    def test_username_length(self):
        result = self.signup._create_account(self.username2, self.password1, self.password2)
        self.assertEqual(result, "Tunnuksen vähimmäispituus on 3 merkkiä")
    
    def test_password_length(self):
        result = self.signup._create_account(self.username, "123", "123")
        self.assertEqual(result, "Salasanan vähimmäispituus on 8 merkkiä")