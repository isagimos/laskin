### Luokan UI suunnittelussa on hyödynnetty kurssimateriaalia: https://ohjelmistotekniikka-hy.github.io/python/tkinter

from tkinter import Tk, ttk, Text, messagebox, Toplevel
from services.calculator_logic import CalculatorLogic
import matplotlib.pyplot as plt
import numpy as np
from repositories.calculations_repository import CalculationsRepository


class Calculator:
    def __init__(self, root):
        
        self._root = root
        self._entry = None

        self._calculator_logic = CalculatorLogic()
        self._calculations = CalculationsRepository(self._root)

        self._errormessage = False

    def start(self, username):

        self._username = username
        self._entry = ttk.Entry(master=self._root)

        self._entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self._draw_function = ttk.Label(master=self._root,
                                         text="Anna piirrettävä funktio, f(x)=")

        self._draw_function.grid(row=8, column=4, columnspan=4)

        ### ChatGPT:llä generoitu koodi alkaa

        self._function = ttk.Entry(master=self._root, width=30)
        self._function.grid(row=9, column=4, columnspan=4)

        self._draw_button = ttk.Button(master=self._root, text="Piirrä funktion kuvaaja", command=lambda: self._draw())

        self._draw_button.grid(row=10, column=4, columnspan=4)

        self._history_box = Text(master=self._root, height=10, width=30)
        self._history_box.grid(row=1, column=5, rowspan=4, padx=5, pady=5)
        self._history_box.config(state="disabled")

        ### ChatGPT:llä generoitu koodi päättyy

        self._instructions = ttk.Button(master=self._root, text="Näytä ohje", command=lambda: self.show_instructions())

        self._instructions.grid(row=11, column=4, columnspan=4)

        self.print_calculations()
        self.add_numbers()
        self.add_operators_and_result()

        self._username_label = ttk.Label(master=self._root,
                                         text=f"Olet kirjautunut sisään käyttäjänä {self._username}.")
        self._username_label.grid(row=6, columnspan=4)

        self._logout = ttk.Button(master=self._root, text="Kirjaudu ulos", command=lambda: self._logging_out())
        self._logout.grid(row=7, columnspan=4)

    ### ChatGPT:llä generoitu koodi alkaa
    def show_instructions(self):
        
        instructions_window = Toplevel(self._root)
        instructions_window.title("Funktion piirtäminen")
        instructions_window.geometry("400x200")
        
        instruction_text = (
            "- Potenssifunktio x² annetaan muodossa x**2\n"
            "- Trigonometriset funktiot: sin(x), cos(x), tan(x)\n"
            "- Eksponenttifunktio e^x: exp(x)\n"
            "- Neliöjuuri: sqrt(x)\n"
            "- Logaritmi: log(x)\n\n"
            "Esimerkkifunktio: -(x-4)**3+x**2-sin(x)+exp(x)"
        )
        
        instructions_label = ttk.Label(instructions_window, text=instruction_text, justify="left")
        instructions_label.grid(row=12, padx=10, pady=10)
    ### ChatGPT:llä generoitu koodi päättyy

    def _draw(self):
        function = self._function.get()
        self._calculator_logic._draw(function)

    def print_calculations(self):
        calculations = self._fetch_history(self._username)

        calculations.reverse()

        ### ChatGPT:llä generoitu koodi alkaa
        self._history_box.config(state="normal")
        self._history_box.delete("1.0", "end")

        for calculation in calculations:
            self._history_box.insert("end",
                                     str(calculation[0]) +
                                     str(calculation[1]) +
                                     str(calculation[2]) + "\n")

        self._history_box.config(state="disabled")
        ### ChatGPT:llä generoitu koodi päättyy        

    def _fetch_history(self, username):

        return self._calculations.fetch_history(username)

    def _handle_button_click(self, button):

        entry_value = self._entry.get()

        result = self._calculator_logic.handle_click(entry_value, button, self._username)
        
        self.update_entry(result)

        if button == "=":
            self.print_calculations()

    ### ChatGPT:llä generoitu koodi alkaa

    def update_entry(self, update):

        self._entry.config(state="normal")
        self._entry.delete(0, "end")
        self._entry.insert(0, update)
        self._entry.config(state="readonly")

    ### ChatGPT:llä generoitu koodi päättyy

    def _logging_out(self):
        from login_view import Login
        self._login = Login(self._root)

        self.destroy_calculator_view()

        self._login.start()
    
    def add_numbers(self):

        self._number0 = ttk.Button(master=self._root, text="0", command=lambda: self._handle_button_click("0"))
        self._number1 = ttk.Button(master=self._root, text="1", command=lambda: self._handle_button_click("1"))
        self._number2 = ttk.Button(master=self._root, text="2", command=lambda: self._handle_button_click("2"))
        self._number3 = ttk.Button(master=self._root, text="3", command=lambda: self._handle_button_click("3"))
        self._number4 = ttk.Button(master=self._root, text="4", command=lambda: self._handle_button_click("4"))
        self._number5 = ttk.Button(master=self._root, text="5", command=lambda: self._handle_button_click("5"))
        self._number6 = ttk.Button(master=self._root, text="6", command=lambda: self._handle_button_click("6"))
        self._number7 = ttk.Button(master=self._root, text="7", command=lambda: self._handle_button_click("7"))
        self._number8 = ttk.Button(master=self._root, text="8", command=lambda: self._handle_button_click("8"))
        self._number9 = ttk.Button(master=self._root, text="9", command=lambda: self._handle_button_click("9"))

        self._number1.grid(row=3, column=0)
        self._number2.grid(row=3, column=1)
        self._number3.grid(row=3, column=2)
        self._number4.grid(row=2, column=0)
        self._number5.grid(row=2, column=1)
        self._number6.grid(row=2, column=2)
        self._number7.grid(row=1, column=0)
        self._number8.grid(row=1, column=1)
        self._number9.grid(row=1, column=2)
        self._number0.grid(row=4, column=1)
    
    def add_operators_and_result(self):

        self._plus = ttk.Button(master=self._root, text="+", command=lambda: self._handle_button_click("+"))
        self._minus = ttk.Button(master=self._root, text="-", command=lambda: self._handle_button_click("-"))
        self._multiply = ttk.Button(master=self._root, text="*", command=lambda: self._handle_button_click("*"))
        self._divide = ttk.Button(master=self._root, text="/", command=lambda: self._handle_button_click("/"))
        self._result = ttk.Button(master=self._root, text="=", command=lambda: self._handle_button_click("="))
        self._decimalpoint = ttk.Button(master=self._root, text=".", command=lambda: self._handle_button_click("."))
        self._backspace = ttk.Button(master=self._root, text="<-", command=lambda: self._handle_button_click("<-"))
        self._clear = ttk.Button(master=self._root, text="C", command=lambda: self._handle_button_click("C"))

        self._backspace.grid(row=4, column=0)
        self._plus.grid(row=1, column=4)
        self._minus.grid(row=2, column=4)
        self._multiply.grid(row=3, column=4)
        self._divide.grid(row=4, column=4)
        self._result.grid(row=5, column=4)
        self._decimalpoint.grid(row=4, column=2)
        self._clear.grid(row=5, column=0)
    
    def destroy_calculator_view(self):

        self._number0.destroy()
        self._number1.destroy()
        self._number2.destroy()
        self._number3.destroy()
        self._number4.destroy()
        self._number5.destroy()
        self._number6.destroy()
        self._number7.destroy()
        self._number8.destroy()
        self._number9.destroy()

        self._entry.destroy()
        self._logout.destroy()

        self._plus.destroy()
        self._minus.destroy()
        self._multiply.destroy()
        self._divide.destroy()
        self._result.destroy()
        self._username_label.destroy()
        self._decimalpoint.destroy()
        self._history_box.destroy()
        self._backspace.destroy()
        self._clear.destroy()

        self._draw_function.destroy()
        self._function.destroy()
        self._draw_button.destroy()
        self._instructions.destroy()