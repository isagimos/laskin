import os
from werkzeug.security import generate_password_hash

class SignUp:
    def __init__(self, root):
        self._root = root

        self.dir = "data"
        self.file = "users.csv"


    def _create_account(self, username, password1, password2):

        if self._check_if_unique(username):
            if password1 == password2:
                self._add_username_and_password(username, password1)
                return "Tunnus luotu"
            return "Salasanat eivät täsmää"
        return "Tunnus on jo käytössä"


    def _check_if_unique(self, username):
        try:
            file_path = os.path.join(self.dir, self.file)
            with open(file_path, "r", encoding="utf-8") as f:
                for row in f:
                    row = row.replace("\n", "")
                    info = row.split(";")
                    username_from_file = info[0]

                    if username == username_from_file:
                        return False
                return True
        except FileNotFoundError:
            return True
    def _add_username_and_password(self, username, password):
        ### ChatGPT:llä generoitu koodi alkaa
        file_path = os.path.join("data", "users.csv")
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                newuser = f"{username};{generate_password_hash(password)}"
                f.write(newuser + "\n")
                return True
        except FileNotFoundError:
            with open(file_path, "w", encoding="utf-8") as f:
        ### ChatGPT:llä generoitu koodi päättyy
                newuser = f"{username};{generate_password_hash(password)}"
                f.write(newuser + "\n")
                return True
        