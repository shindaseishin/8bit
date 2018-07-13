import curses

import const

class Component(object):
    def __init__(self, window, led_colour, label, bit_width):
        self._window        = window
        self._label         = label
        self._led_colour    = led_colour
        self._bit_width     = int(bit_width)
        self._format_string = "0{}b".format(self._bit_width)
        self._bit_mask      = 2**bit_width - 1
        self._cur_value     = 0

        self._window.box()
        self._window.addstr(0, 2, " " + self._label + " ")
        self.display()


    def display(self):
        self._window.addstr(2, 2, self.decode_binary(), curses.color_pair(self._led_colour) | curses.A_BOLD)
        self._window.refresh()


    def decode_binary(self, value=None):
        if value == None:
            value = self._cur_value

        binary = format(value, self._format_string)
        string = ""
        for i in binary:
            if i == '0':
                string = string + const.LED_OFF
            else:
                string = string + const.LED_ON
        return string

    def read_value(self):
        return self._cur_value


    def latch_value(self, value):
        self._cur_value = value & self._bit_mask


    def reset(self):
        self.latch_value(0)
