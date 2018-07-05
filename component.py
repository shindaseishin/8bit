import curses

import const

class Component(object):
    def __init__(self, window, led_colour, label, bit_width):
        self._window        = window
        self._label         = label
        self._led_colour    = led_colour
        self._bit_width     = int(bit_width)
        self._format_string = "0{}b".format(self._bit_width)
        self._cur_value     = 0

        self._window.box()
        self._window.addstr(0, 2, " " + self._label + " ")
        self.display()


    def display(self):
        self._window.addstr(2, 2, self.decode_binary(),    curses.color_pair(self._led_colour) | curses.A_BOLD)
        self._window.refresh()


    def decode_binary(self):
        binary = format(self._cur_value, self._format_string)
        string = ""
        for i in binary:
            if i == '0':
                string = string + const.LED_OFF
            else:
                string = string + const.LED_ON
        return string

    def reset(self):
        self._cur_value = 0
