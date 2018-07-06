import curses

from eventtypes import ClockPulse
from component import Component
import const

class Output(Component):

#      _      __  __       __  _   __  _   _ 
# ___ / \ /|   _) __) |_| |_  |_    / (_) (_|
#     \_/  |  /__ __)   | __) |_)  /  (_)  _|

    digits = {
        '-': ["   ", "___",  "   "],
        '0': [" _ ", "/ \\", "\\_/"],
        '1': ["   ","/| "," | "],
        '2': ["__ "," _)","/__"],
        '3': ["__ ","__)","__)"],
        '4': ["   ","|_|","  |"],
        '5': [" __","|_ ","__)"],
        '6': [" _ ","|_ ","|_)"],
        '7': [" __","  /"," / "],
        '8': [" _ ","(_)","(_)"],
        '9': [" _ ","(_|"," _|"],
    }
    
    def __init__(self, window):
        Component.__init__(self, window, const.COLOR_PAIR_RED, 'Output', 8)


    def display(self):
        strnum = "{:04}".format(self._cur_value)
        for i in range(4):
            c = strnum[i]
            for j in range(3):
                self._window.addstr(1+j, 2 + i*4+ i, Output.digits[c][j], curses.color_pair(self._led_colour) | curses.A_BOLD)
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

