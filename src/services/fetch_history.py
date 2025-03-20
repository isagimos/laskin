class FetchHistory:
    def __init__(self, root, username):
        self._root = root
        self._username = username

        self._calculations = []
    def _fetch_history(self):
        try:
            with open("calculations.csv", "r", encoding="utf-8") as f:
                for row in f:
                    row = row.replace("\n", "")
                    calculation = row.split(";")
                    if calculation[0] == self._username:
                        self._calculations.append(calculation[1:])
            return self._calculations
        except FileNotFoundError:
            return self._calculations
        