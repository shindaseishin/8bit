import curses

from eventtypes import ClockPulse
from component import Component
import const

class Output(Component):
    MODE_NORMAL = 0
    MODE_TWOS_COMPLEMENT = 1
#      _      __  __       __  _  ___  _   _
#  __ / \ /|   _) __) |_| |_  |_    / (_) (_|
#     \_/  |  /__ __)   | __) |_)  /  (_)  _)

    digits = {
        '-': ["   ", " __",  "   "],
        '0': [" _ ", "/ \\", "\\_/"],
        '1': ["   ","/| "," | "],
        '2': ["__ "," _)","/__"],
        '3': ["__ ","__)","__)"],
        '4': ["   ","|_|","  |"],
        '5': [" __","|_ ","__)"],
        '6': [" _ ","|_ ","|_)"],
        '7': ["___","  /"," / "],
        '8': [" _ ","(_)","(_)"],
        '9': [" _ ","(_|"," _)"],
    }

    def __init__(self, window, signal=None, data=None):
        self._mode = Output.MODE_NORMAL
        super().__init__(window, const.COLOR_PAIR_RED, 'Output', 8, signal=signal, data=data)


    def display(self):
        if self._mode == Output.MODE_TWOS_COMPLEMENT and self._cur_value < 0:
            for j in range(3):
                self._window.addstr(1+j, 2, Output.digits['-'][j], curses.color_pair(self._led_colour) | curses.A_BOLD)
        strnum = "{:03}".format(self._cur_value)
        for i in range(3):
            c = strnum[i]
            for j in range(3):
                self._window.addstr(1+j, 6 + i*4+ i, Output.digits[c][j], curses.color_pair(self._led_colour) | curses.A_BOLD)
        self._window.refresh()


    def clock_read(self, event):
        if isinstance(event, ClockPulse) and event.state == 1:
            if self._signals.read_signal('OI'):
                self.assert_value(self._data.read_value())
                return
