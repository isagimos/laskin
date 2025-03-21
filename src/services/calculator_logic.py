import os
import sympy as sp

class CalculatorLogic:
    def __init__(self):
        self._root = self
    
    def handle_click(self, entry_value, button, username):
        if entry_value == "Virhe":
            entry_value = ""
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