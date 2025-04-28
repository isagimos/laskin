import os
class CalculationsRepository:
    """This class manages the calculations saved to the csv-file.
    """
    def __init__(self, root):
        """The constructor of the class. Defines the directory of the csv-file.

        Args:
            dir: Directory
            file: Name of the csv-file.
            file_path: The path for the csv-file.
        """
        self._root = root


        self.dir = "data"
        self.file = "calculations.csv"

        ### ChatGPT:llä generoitu koodi alkaa
        self.file_path = "data/calculations.csv"
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        ### ChatGPT:llä generoitu koodi päättyy

    def fetch_history(self, username):
        """Retrieves from the csv-file the calculations of a certain user.

        Args:
            username: Username of the current logged in user of the calculator.

        Returns:
            calculations: List of all calculations performed by the user.
        """

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
        """Add calculation to csv-file.

        Args:
            username: Logged in user.
            entry_value: The calculation performed by the user. Contains operators and operands.
            result: The result of the calculation. If the input is invalid, the result is "Virhe".

        Returns:
            Returns True.
        """

        file_path = os.path.join("data", "calculations.csv")
        with open(file_path, "a", encoding="utf-8") as f:
            newrow = f"{username};{entry_value};=;{result};"
            f.write(newrow + "\n")
        return True
