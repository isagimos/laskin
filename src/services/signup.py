from tkinter import Tk, ttk
from werkzeug.security import generate_password_hash

class SignUp:
    def __init__(self, root):
        self._root = root


    def _create_account(self, username, password1, password2):

        if self._check_if_unique(username):
            if password1 == password2:
                self._add_username_and_password(username, password1)
                return "Tunnus luotu"
            else:
                return "Salasanat eivät täsmää"
        else:
            return "Tunnus on jo käytössä"


    def _check_if_unique(self, username):
        with open("users.csv", "r") as f:
            for row in f:
                row = row.replace("\n", "")
                info = row.split(";")
                username_from_file = info[0]

                if username == username_from_file:
                    return False
            return True
    
    def _add_username_and_password(self, username, password):
        with open("users.csv", "a") as f:
            
            newuser = f"{username};{generate_password_hash(password)}"
            f.write(newuser + "\n")
            return True