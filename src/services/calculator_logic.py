"""

Tämän tiedoston koodin pohjana on seuraava ChatGPT:llä luotu luokka:

class CalculatorLogic:
    def __init__(self):
        self._first_operand = None
        self._second_operand = None
        self._operator = None

    def handle_operand(self, operand):
        # Laskentatoiminnot
        pass
    
    def calculate(self):
        # Laskeminen ensimmäisellä ja toisella operandilla
        pass

Olen täydentänyt koodin itse. Aluksi koodaamani metodi handle_click palautti vain True tai None
(esim. entry_value + button sijaan), mutta muutin tämän ChatGPT:ltä saamani ohjeen mukaan,
jolloin sain vuorovaikutuksen toimimaan sovelluslogiikan ja käyttöliittymälogiikan välille.
Selkeyden vuoksi en kommentoinut näitä muutoksia itse koodiin.
        
"""

import os

class CalculatorLogic:
    def __init__(self):

        self._first_operand = None
        self._second_operand = None
        self._operator = None

        self._point_in_first_operand = False
        self._point_in_second_operand = False



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
            if len(entry_value) == 1 and entry_value[0] == "0":
                return button
            
            if self._first_operand != None:
                if entry_value[-2] in self._operators and entry_value[-1] == "0":
                    return entry_value[:-1] + button
            
            return entry_value + button
        
        if button == ".":
            if self._first_operand == None:
                if self._point_in_first_operand == False:
                    self._point_in_first_operand = True
                    return entry_value + button
                
            else:
                if self._point_in_second_operand == False:
                    self._point_in_second_operand = True
                    return entry_value + button
            
            return entry_value
        


        # If the user clicks an operand button, save the first operand and the operator:
        if button in self._operators:
            # Return if the user has already clicked an operator button:
            if self._operator is not None:
                return entry_value
            self._first_operand = entry_value
            self._operator = button

            return entry_value + button
        

        # If the user clicks "=", save the second operand, calculate and save to file:
        if button == "=":

            try:
                self._second_operand = entry_value.split(f"{self._operator}")[1]
            except IndexError:
                self._first_operand = None
                self._second_operand = None
                self._operator = None

                self._point_in_first_operand = False
                self._point_in_second_operand = False
                return "Virhe"
            
            if self._second_operand == "":
                return entry_value
            result = self.calculate(self._first_operand, self._second_operand, self._operator)
            file_path = os.path.join("data", "calculations.csv")
            with open(file_path, "a", encoding="utf-8") as f:
                newrow = f"{username};{self._first_operand};{self._operator};"
                newrow += f"{self._second_operand};=;{result}"
                f.write(newrow + "\n")

            self._first_operand = None
            self._second_operand = None
            self._operator = None
            return result
    def calculate(self, first_operand, second_operand, operator):

        try:
            first_operand = float(first_operand)
            second_operand = float(second_operand)
        except ValueError:
            return "Virhe"

        if operator == "+":
            return first_operand + second_operand
        if operator == "-":
            return first_operand - second_operand
        if operator == "*":
            return first_operand * second_operand
        if operator == "/":
            try:
                return first_operand / second_operand
            except ZeroDivisionError:
                self._first_operand = None
                self._second_operand = None
                self._operator = None

                self._point_in_first_operand = False
                self._point_in_second_operand = False
                return "Virhe"