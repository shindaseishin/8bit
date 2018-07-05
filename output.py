import curses

from eventtypes import ClockPulse
from component import Component
import const

class Output(Component):
    def __init__(self, window, led_colour, label, bit_width):


    def display(self):
        self._window.addstr(2, 2, self.decode_binary(), curses.color_pair(self._led_colour) | curses.A_BOLD)
        self._window.refresh()


    def assert_value(self, value):
        self._cur_value = value & self._bit_mask
        self.display()


    def reset(self):
        self.assert_value(0)
        self.display()


    def receive_clock(self, event):
        if isinstance(event, ClockPulse):
            self.assert_value(self._cur_value+1)


    def reset(self):
        self.assert_value(0)


##############
#
# /--\    | ---- ---\ |  | ---- /--\ ---- /--\ /--\
# |  |    |    |    | |  | |    |       | |  | |  |
# |  |    | ----  --< \--| ---\ >--\   /  >--< \--/
# |  |    | |       |    |    | |  |   |  |  |    |
# \--/    | ---- ---/    | ---/ \--/   |  \--/ \--/
#
##############
