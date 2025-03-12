### Luokan UI suunnittelussa on hyödynnetty kurssimateriaalia: https://ohjelmistotekniikka-hy.github.io/python/tkinter

from tkinter import Tk, ttk
from calculator import Calculator

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_calculator_view()
    
    def _show_calculator_view(self):
        self._current_view = Calculator(self._root)

window = Tk()
window.title("Laskin")

ui = UI(window)
ui.start()

window.mainloop()