from tkinter import Tk, ttk
from calculator_view import Calculator
from signup_view import CreateAccount

class Login:
    def __init__(self, root):
        self._root = root

        self._username = None
        self._password = None

        self._calculator = Calculator(self._root)

        self._signup = CreateAccount(self._root)
    
    def start(self):

        # GitHub Copilotin vinkistä tehty muuttujista instanssimuuttujia lisäämällä self._-etuliite

        self._username_label = ttk.Label(master=self._root, text="Käyttäjänimi: ")
        self._password_label = ttk.Label(master=self._root, text="Salasana: ")

        self._username_entry = ttk.Entry(master=self._root)
        self._password_entry = ttk.Entry(master=self._root)

        # GitHub Copilotilla generoitu koodi alkaa
        self._login_button = ttk.Button(master=self._root, text="Kirjaudu sisään",
                                        command=lambda: self._handle_login(self._username_entry.get(), self._password_entry.get()))
        # GitHub Copilotilla generoitu koodi päättyy

        self._signup_button = ttk.Button(master=self._root, text="Luo tunnus",
                                        command=lambda: self._create_account())

        self._username_label.grid(row=0, column=0)
        self._password_label.grid(row=1, column=0)

        self._username_entry.grid(row=0, column=1)
        self._password_entry.grid(row=1, column=1)

        self._login_button.grid(row=2, column=0, columnspan=2)
        self._signup_button.grid(row=3, column=0, columnspan=2)

    # GitHub Copilotilla generoitu koodi alkaa
    def _handle_login(self, username, password):

        self._username = username
        self._password = password

        from services.login import LoginCheck

        self._login_check = LoginCheck(self._root)


        result = self._login_check._check_username_and_password(username, password)

        print(result)

        if result == True:

            self._destroy_login_view()

            self._calculator.start(self._username)
        
        else:
            try:
                self._error_label.destroy()
            except:
                pass
            self._error_label = ttk.Label(master=self._root, text="Väärä käyttäjätunnus tai salasana")
            self._error_label.grid(row=4, columnspan=2)

    def _destroy_login_view(self):
        
        self._password_label.destroy()
        self._username_entry.destroy()
        self._password_entry.destroy()
        self._login_button.destroy()
        self._username_label.destroy()
    # GitHub Copilotilla generoitu koodi päättyy        
        self._signup_button.destroy()
        try:
            self._error_label.destroy()
        except:
            pass

    def _create_account(self):

        self._destroy_login_view()

        self._signup.start()

