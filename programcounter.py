from component import Component
import const

class ProgramCounter(Component):
    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_BLUE, 'Program Counter', 8)

    def step(self):
        self.latch_value(self._cur_value+1)
