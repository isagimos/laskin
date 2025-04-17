import os
class CalculationsRepository:
    def __init__(self, root):
        self._root = root


        self.dir = "data"
        self.file = "calculations.csv"

        ### ChatGPT:llä generoitu koodi alkaa
        self.file_path = "data/calculations.csv"
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        ### ChatGPT:llä generoitu koodi päättyy

        self._calculations = []

    def fetch_history(self, username):
        try:
            file_path = os.path.join("data", "calculations.csv")
            with open(file_path, "r", encoding="utf-8") as f:
                for row in f:
                    row = row.replace("\n", "")
                    calculation = row.split(";")
                    if calculation[0] == username:
                        self._calculations.append(calculation[1:])
            return self._calculations
        except FileNotFoundError:
            return self._calculations
        