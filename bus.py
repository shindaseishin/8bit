from component import Component

import const

class Bus(Component):

    def __init__(self, window, led_colour, label, bit_width):
        Component.__init__(self, window, led_colour, label, bit_width)


    def assert_value(self, new_value):
        self._cur_value = new_value
        self.display()
