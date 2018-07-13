from component import Component

import const
from eventtypes import ClockPulse

class Alu(Component):
    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_RED, 'ALU', 8)


    def operate(reg_a, reg_b, data_bus, operation):
        a = reg_a.read_value()
        b = reg_b.read_value() * operation
        data_bus.latch_value(a + b)
