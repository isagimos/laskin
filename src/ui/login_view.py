from tkinter import ttk
from calculator_view import Calculator
from signup_view import CreateAccount

class Login:
    """A user interface class. Shows the log in view at launchup of the application.
    """

    def __init__(self, root):
        """The constructor of the class.

        Args:
            username: Username of current user (None at start)
            password: Password of curren user (None at start)
            _calculator: class Calculator from calculator_view.py
            _signup: class CreateAccount from signup_view.py
        """
        self._root = root

        self._username = None
        self._password = None

        self._calculator = Calculator(self._root)

        self._signup = CreateAccount(self._root)
    
    def start(self):
        """Shows the login view of the application.
        """

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
        """This method is called when a user tries to log in.

        Args:
            username: Username entered by the user.
            password: Password entered by the user.
        """

        self._username = username
        self._password = password

        from repositories.users_repository import UsersRepository

        self._login_check = UsersRepository(self._root)


        result = self._login_check.check_username_and_password(username, password)

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
        """If user is successfully logged in,
        this method destroys the current login view of the application.
        """
        
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
        """Destroys the current login view and show signup view.
        """

        self._destroy_login_view()

        self._signup.start()

