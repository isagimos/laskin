### Luokan UI suunnittelussa on hyödynnetty kurssimateriaalia: https://ohjelmistotekniikka-hy.github.io/python/tkinter

from tkinter import Tk, ttk

class UI:
    def __init__(self, root):
        self._root = root
        self._entry = None

        self._first_operand = None
        self._second_operand = None
        self._operator = None

        self._operands = ["+", "-", "*", "/"]

    def start(self):
        self._entry = ttk.Entry(master=self._root)
        number0 = ttk.Button(master=self._root, text="0", command=lambda: self._handle_button_click("0"))
        number1 = ttk.Button(master=self._root, text="1", command=lambda: self._handle_button_click("1"))
        number2 = ttk.Button(master=self._root, text="2", command=lambda: self._handle_button_click("2"))
        number3 = ttk.Button(master=self._root, text="3", command=lambda: self._handle_button_click("3"))
        number4 = ttk.Button(master=self._root, text="4", command=lambda: self._handle_button_click("4"))
        number5 = ttk.Button(master=self._root, text="5", command=lambda: self._handle_button_click("5"))
        number6 = ttk.Button(master=self._root, text="6", command=lambda: self._handle_button_click("6"))
        number7 = ttk.Button(master=self._root, text="7", command=lambda: self._handle_button_click("7"))
        number8 = ttk.Button(master=self._root, text="8", command=lambda: self._handle_button_click("8"))
        number9 = ttk.Button(master=self._root, text="9", command=lambda: self._handle_button_click("9"))

        plus = ttk.Button(master=self._root, text="+", command=lambda: self._handle_button_click("+"))
        minus = ttk.Button(master=self._root, text="-", command=lambda: self._handle_button_click("-"))
        multiply = ttk.Button(master=self._root, text="*", command=lambda: self._handle_button_click("*"))
        divide = ttk.Button(master=self._root, text="/", command=lambda: self._handle_button_click("/"))
        result = ttk.Button(master=self._root, text="=", command=lambda: self._handle_button_click("="))

        self._entry.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        number1.grid(row=3, column=0)
        number2.grid(row=3, column=1)
        number3.grid(row=3, column=2)
        number4.grid(row=2, column=0)
        number5.grid(row=2, column=1)
        number6.grid(row=2, column=2)
        number7.grid(row=1, column=0)
        number8.grid(row=1, column=1)
        number9.grid(row=1, column=2)
        number0.grid(row=4, column=1)

        plus.grid(row=1, column=4)
        minus.grid(row=2, column=4)
        multiply.grid(row=3, column=4)
        divide.grid(row=4, column=4)
        result.grid(row=5, column=4)

    def _handle_button_click(self, button):
        entry_value = self._entry.get()

        # At first the user cannot click an operator of "=" symbol:
        if entry_value == "":
            if button in self._operands or button == "=":
                return
            
        # If the user clicks an operand button, save the first operand and the operator:
        if button in self._operands:
            
            # Return if the user has already clicked an operator button:
            if self._operator != None:
                return
            
            self._first_operand = entry_value
            self._operator = button
            self.update_entry(entry_value, button)

            return
        
        # If the user clicks "=", save the second operand:
        if button == "=":
            self._second_operand = entry_value.split(f"{self._operator}")[1]
            print(self._first_operand)
            print(self._operator)
            print(self._second_operand)

        self.update_entry(entry_value, button)

### Tekoälyllä generoitu koodi alkaa:
    def update_entry(self, entry_value, button):

        self._entry.config(state="normal")  # Tehdään kentästä muokattavissa oleva
        self._entry.delete(0, "end")  # Tyhjennetään nykyinen sisältä
        self._entry.insert(0, entry_value + button)  # Lisätään uuden painikkeen arvo loppuun
        self._entry.config(state="readonly")  # Asetetaan kenttä taas luettavaksi
### Tekoälyllä generoitu koodi päättyy



window = Tk()
window.title("Laskin")

ui = UI(window)
ui.start()

window.mainloop()