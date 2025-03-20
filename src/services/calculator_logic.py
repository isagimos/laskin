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


class CalculatorLogic:
    def __init__(self):

        self._first_operand = None
        self._second_operand = None
        self._operator = None

        self._operators = ["+", "-", "*", "/"]

    def handle_click(self, entry_value, button, username):
        if entry_value == "Nollalla ei voi jakaa":
            entry_value = ""

        # At first the user cannot click an operator or "=" symbol or 0:
        if entry_value == "":
            if button in self._operators or button == "=":
                return entry_value
            if button == "0":
                return entry_value

        # If button is digit and != 0 it is added to the entry_value:
        if button.isdigit():
            return entry_value + button
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

            self._second_operand = entry_value.split(f"{self._operator}")[1]
            if self._second_operand == "":
                return entry_value
            result = self.calculate(self._first_operand, self._second_operand, self._operator)

            with open("calculations.csv", "a", encoding="utf-8") as f:
                newrow = f"{username};{self._first_operand};\
                    {self._operator};{self._second_operand};=;{result}"
                f.write(newrow + "\n")

            self._first_operand = None
            self._second_operand = None
            self._operator = None
            return result
    def calculate(self, first_operand, second_operand, operator):

        first_operand = float(first_operand)
        second_operand = float(second_operand)

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
                return "Nollalla ei voi jakaa"
            