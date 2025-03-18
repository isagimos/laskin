from tkinter import Tk, ttk
from ui.calculator_view import Calculator

class FetchHistory:
    def __init__(self, root, username):
        self._root = root
        self._username = username

        self._calculations = []
    
    def _fetch_history(self):
        with open("calculations.csv", "r") as f:
            for row in f:
                row = row.replace("\n", "")
                calculation = row.split(";")
                if calculation[0] == self._username:
                    self._calculations.append(calculation[1:])
        
        return self._calculations

