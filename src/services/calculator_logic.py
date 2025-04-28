from tkinter import messagebox
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne
from repositories.calculations_repository import CalculationsRepository

class CalculatorLogic:
    """A class to manage the backend functions of the calculator.

    Attributes:
        _calculations: Repository for the calculations.
        _operator: Mathematical operators supported by the calculator.

    """
    def __init__(self):
        """The constructor of the class.

        Args:
            _calculations: Repository for the calculations.
            _operator: Mathematical operators supported by the calculator.
        """
        self._root = self

        self._calculations = CalculationsRepository(self._root)

        self._operators = ["+", "-", "*", "/"]

    def handle_click(self, entry_value, button, username):
        """Responses to the actions of the user of the calculator.

        Args:
            entry_value: The sequence of operators and operands that the user has clicked.
            button: The newest button clicked by the user.
            username: The username of the logged in user of the calculator.

        Returns:
            "": Empty string
            entry_value
            button
            entry_value + button
            result: The result of the calculation, if the user has clicked "="
        """
        if button == "C":
            return ""

        if entry_value == "Virhe":
            if button.isdigit():
                return button
            return ""

        if button == "<-":
            return entry_value[:-1]

        # At first the user cannot click an operator or "=" symbol:
        if entry_value == "":
            if button in self._operators or button == "=":
                return entry_value

        if button.isdigit():
            if entry_value == "0":
                return button
            try:
                if entry_value[-1] == "0" and entry_value[-2] in self._operators:
                    return entry_value[:-1] + button
            except IndexError:
                return entry_value + button

        if button in self._operators:
            if len(entry_value) < 1:
                return entry_value
            if entry_value[-1] in self._operators:
                return entry_value

        if button == ".":
            try:
                if entry_value[-1] == ".":
                    return entry_value
            except IndexError:
                return button

    ### ChatGPT:llä generoitu koodi alkaa
        if button == "=":
            try:
                result = sp.simplify(entry_value)
                if result in {sp.zoo, sp.nan, sp.oo, -sp.oo}:
                    result = "Virhe"

                result = float(result)

            except (SyntaxError, ValueError):
                result = "Virhe"

            self._calculations.add_calculation(username, entry_value, result)

            try:
                return f"{result:.10g}"
            except ValueError:
                return result

        return entry_value + button

    def _draw(self, function):
        """Draws a graph of a mathematical function according to the input of the user.

        Args:
            function: The mathematical function given by the user of the calculator.

        Returns:
            True: The graph is showed
            False: The graph is not showed; error in the input.
        """
        x = np.linspace(-10, 10, 400)
        try:
            y = ne.evaluate(function, local_dict={"x": x})
            plt.plot(x, y)
            plt.title(f"f(x) = {function}")
            plt.grid(True)
            plt.show()
            return True
        except (SyntaxError, TypeError, ValueError, NameError, KeyError):
            messagebox.showerror("Virhe", "Virheellinen syöte")
            return False
    ### ChatGPT:llä generoitu koodi päättyy
