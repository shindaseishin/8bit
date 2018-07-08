from component import Component

import const

class Alu(Component):
    def __init__(self, window, reg_a, reg_b, signal=None, data=None):
        super().__init__(window, const.COLOR_PAIR_RED, 'ALU', 8, signal=signal, data=data)
        self._reg_a = reg_a
        self._reg_b = reg_b

    def clock_write(self, event):
        if self._signals.read_signal('EO'):
            self._data.assert_value(self._cur_value)

    def clock_read(self, event):
        a = self._reg_a.read_value()
        b = self._reg_b.read_value()
        
        if self._signals.read_signal('SU'):
            self.assert_value(a-b)
        else:
            self.assert_value(a+b)
        
        
    def assert_value(self, value):
        super().assert_value(value)

