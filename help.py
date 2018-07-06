from component import Component
import const

class Help(Component):

    def __init__(self, window):
        self._window = window
        super().__init__(self._window, const.COLOR_PAIR_WHITE, "Help", 0)


    def display(self):
        self._window.addstr(2, 2, "[q] Quit\t[p] Pause\t[h] Halt\t[r] Reset")
        self._window.addstr(3, 2, "[a] Faster\t[z] Slower\t")
        self._window.refresh()


    def assert_value(self, value):
        pass
