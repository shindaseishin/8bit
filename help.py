from component import Component
import const

class Help(Component):

    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_WHITE, "Help", 0)


    def display(self):
        self._window.addstr(2, 2, "[q] Quit\t[p] Pause\t[h] Halt\t[r] Reset")
        self._window.addstr(3, 2, "[a] Faster\t[z] Slower\t[o] Pulse")
        self._window.addstr(4, 2, "[\u2191] Scroll Up\t[\u2193] Scroll Down")


    def latch_value(self, value):
        pass
