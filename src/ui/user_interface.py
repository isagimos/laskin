### Luokan UI suunnittelussa on hyödynnetty kurssimateriaalia: https://ohjelmistotekniikka-hy.github.io/python/tkinter

### ChatGPT:llä generoitu koodi alkaa:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
### ChatGPT:llä generoitu koodi päättyy

from tkinter import Tk, ttk
from calculator_view import Calculator

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_calculator_view()
    
    def _show_calculator_view(self):
        self._current_view = Calculator(self._root)
        ### ChatGPT:llä generoitu koodi alkaa
        self._current_view.start()
        ### ChatGPT:llä generoitu koodi päättyy
window = Tk()
window.title("Laskin")

ui = UI(window)
ui.start()

window.mainloop()