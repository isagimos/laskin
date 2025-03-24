import os
import sympy as sp

class CalculatorLogic:
    def __init__(self):
        self._root = self

        self._operators = ["+", "-", "*", "/"]
    
    def handle_click(self, entry_value, button, username):
        if entry_value == "Virhe":
            entry_value = ""
            return button
        
        # At first the user cannot click an operator or "=" symbol:
        if entry_value == "":
            if button in self._operators or button == "=":
                return entry_value
            
        if button.isdigit():
            if entry_value == "0":
                return button
            #if len(entry_value) == 1 and entry_value[-1] == "0":
            try:
                if entry_value[-1] == "0" and entry_value[-2] in self._operators:
                    return entry_value[:-1] + button
            except IndexError:
                return entry_value + button
        
        if button in self._operators:
            if len(entry_value) < 1:
                return entry_value
            else:
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
                if result == sp.zoo or result == sp.oo or result == -sp.oo:     #
                    result = "Virhe"                                            #
                                                                                #
                result = float(result)                                          #
    
            except:                                                             #
                result = "Virhe"                                                #

            file_path = os.path.join("data", "calculations.csv")
            with open(file_path, "a", encoding="utf-8") as f:
                newrow = f"{username};{entry_value};=;{result};"
                f.write(newrow + "\n")

            try:                                                                #
                return f"{result:.10g}"                                         #
            except:                                                             #
                return result                                                   #
            
        return entry_value + button
### ChatGPT:llä generoitu koodi päättyy