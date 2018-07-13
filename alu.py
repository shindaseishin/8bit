from component import Component

import const
from eventtypes import ClockPulse

class Alu(Component):
    OPERATION_ADD = 1
    OPERATION_SUB = -1

    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_RED, 'ALU', 8)


    def operate(self, a, b, operation):
        b = b * operation
        self.latch_value(a + b)
