from component import Component
from eventtypes import ClockPulse
import const

class ProgramCounter(Component):
    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_BLUE, 'Program Counter', 8)
