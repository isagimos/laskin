from repositories.users_repository import UsersRepository

class SignUp:
    def __init__(self, root):
        self._root = root
        self._users_repository = UsersRepository(self._root)

    def _create_account(self, username, password1, password2):

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

        return self._users_repository.check_username(username)

    def _add_username_and_password(self, username, password):

        return self._users_repository.add_username_and_password(username, password)

    def _check_username_length(self, username):
        if len(username) < 3:
            return False
        return True
