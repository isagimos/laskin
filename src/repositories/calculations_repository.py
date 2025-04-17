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

    def fetch_history(self, username):
        calculations = []
        try:
            file_path = os.path.join("data", "calculations.csv")
            with open(file_path, "r", encoding="utf-8") as f:
                for row in f:
                    row = row.replace("\n", "")
                    calculation = row.split(";")
                    if calculation[0] == username:
                        calculations.append(calculation[1:])
            return calculations
        except FileNotFoundError:
            return calculations

    def add_calculation(self, username, entry_value, result):

        file_path = os.path.join("data", "calculations.csv")
        with open(file_path, "a", encoding="utf-8") as f:
            newrow = f"{username};{entry_value};=;{result};"
            f.write(newrow + "\n")
        return True
