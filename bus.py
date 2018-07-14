from component import Component

class Bus(Component):

    def __init__(self, window, led_colour, label, bit_width):
        super().__init__(window, led_colour, label, bit_width)
