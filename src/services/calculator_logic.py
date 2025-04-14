import os
from tkinter import messagebox
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import numexpr as ne

class CalculatorLogic:
    def __init__(self):
        self._root = self

        self._operators = ["+", "-", "*", "/"]

    def handle_click(self, entry_value, button, username):
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

### Tästä etenpäin ChatGPT:llä generoitua koodia riveillä, jotka merkitty #:
        if button == "=":
            try:                                                                #
                result = sp.simplify(entry_value)                               #
                if result in {sp.zoo, sp.nan, sp.oo, -sp.oo}:                   #
                    result = "Virhe"                                            #
                                                                                #
                result = float(result)                                          #

            except (SyntaxError, ValueError):                                   #
                result = "Virhe"                                                #

            file_path = os.path.join("data", "calculations.csv")
            with open(file_path, "a", encoding="utf-8") as f:
                newrow = f"{username};{entry_value};=;{result};"
                f.write(newrow + "\n")

            try:                                                                #
                return f"{result:.10g}"                                         #
            except ValueError:                                                  #
                return result                                                   #

        return entry_value + button

    ### ChatGPT:llä generoitu koodi alkaa
    def _draw(self, function):
        x = np.linspace(-10, 10, 400)
        try:
            y = ne.evaluate(function, local_dict={"x": x})
            plt.plot(x, y)
            plt.title(f"f(x) = {function}")
            plt.grid(True)
            plt.show()
            return True
        except (SyntaxError, ValueError, NameError, KeyError):
            messagebox.showerror("Virhe", "Virheellinen syöte")
            return False
    ### ChatGPT:llä generoitu koodi päättyy
