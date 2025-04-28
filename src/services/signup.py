from repositories.users_repository import UsersRepository

class SignUp:
    """A backend class for creating a new account.

    Attributes:
        _users_repository: Repository for handling the registered users.
    """

    def __init__(self, root):
        """The constructor of the class.

        Attributes:
            _users_repository: Repository for handling the registered users.
        """

        self._root = root
        self._users_repository = UsersRepository(self._root)

    def _create_account(self, username, password1, password2):
        """Method for creating a new account.

        Args:
            username: The username chosen by the user.
            password1: The password given by the user.
            password2 Re-entered password.

        Returns:
            Returns feedback to the user. For example, if the username is too short
            (less than 3 characters), the user will see a notification.
        """

        if not self._check_username_length(username):
            return "Tunnuksen vähimmäispituus on 3 merkkiä"

        if self._check_if_unique(username):
            if password1 == password2:
                if len(password1) < 8:
                    return "Salasanan vähimmäispituus on 8 merkkiä"
                self._add_username_and_password(username, password1)
                return "Tunnus luotu"
            return "Salasanat eivät täsmää"
        return "Tunnus on jo käytössä"

    def _check_if_unique(self, username):
        """Check if the username is unique or already taken by somebody else.

        Args:
            username: The username inputted by the user.

        Returns:
            True or False from the method check_username in the class UsersRepository.
            If username is unique, the return value is True. If not, False.
        """

        return self._users_repository.check_username(username)

    def _add_username_and_password(self, username, password):
        """Add new username and password to repository, if the username is unique.

        Args:
            username: Username given by the user.
            password: Password given by the user.

        Returns:
            Always returns True.
        """

        return self._users_repository.add_username_and_password(username, password)

    def _check_username_length(self, username):
        """Check the length of the given username.

        Args:
            username: Username given by the user.

        Returns:
            False, if the username is shorten than 3 characters. Otherwise, return True.
        """
        
        if len(username) < 3:
            return False
        return True
