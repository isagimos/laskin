import os
from werkzeug.security import check_password_hash, generate_password_hash

class UsersRepository:
    def __init__(self, root):
        self._root = root

        self.dir = "data"
        self.file = "users.csv"

        ### ChatGPT:llä generoitu koodi alkaa
        self.file_path = "data/users.csv"
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        ### ChatGPT:llä generoitu koodi päättyy


    def check_username_and_password(self, username, password):
        try:
            file_path = os.path.join("data", "users.csv")
            with open(file_path, "r", encoding="utf-8") as f:
                for row in f:
                    row = row.replace("\n", "")
                    info = row.split(";")
                    username_from_file = info[0]
                    if username_from_file == username:
                        if check_password_hash(info[1], password):
                            return True
        except FileNotFoundError:
            return "Väärä käyttäjätunnus tai salasana"
        return "Väärä käyttäjätunnus tai salasana"

    def check_username(self, username):

        try:
            self.file_path = os.path.join(self.dir, self.file)
            with open(self.file_path, "r", encoding="utf-8") as f:
                for row in f:
                    row = row.replace("\n", "")
                    info = row.split(";")
                    username_from_file = info[0]

                    if username == username_from_file:
                        return False
                return True
        except FileNotFoundError:
            return True

    def add_username_and_password(self, username, password):
        ### ChatGPT:llä generoitu koodi alkaa
        self.file_path = os.path.join("data", "users.csv")
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                newuser = f"{username};{generate_password_hash(password)}"
                f.write(newuser + "\n")
                return True
        except FileNotFoundError:
            with open(self.file_path, "w", encoding="utf-8") as f:
        ### ChatGPT:llä generoitu koodi päättyy
                newuser = f"{username};{generate_password_hash(password)}"
                f.write(newuser + "\n")
                return True
    