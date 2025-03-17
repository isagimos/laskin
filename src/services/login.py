from tkinter import Tk, ttk
from ui.login_view import Login
from werkzeug.security import check_password_hash

class LoginCheck:
    def __init__(self, root):
        self._root = root

    def _check_username_and_password(self, username, password):
        with open("users.csv", "r") as f:
            print("tänne tullaan")
            for row in f:
                row = row.replace("\n", "")
                info = row.split(";")
                print(info)
                username_from_file = info[0]
                if username_from_file == username:
                    print("käyttäjätunnus moi löytyi")
                    print("annettu salasana: ", password)
                    if check_password_hash(info[1], password):
                        return True
        return False