from component import Component
from eventtypes import ClockPulse
import const

class Register(Component):
    def __init__(self, window, label, val_latch, val_assert, signal=None, data=None):
        super().__init__(window, const.COLOR_PAIR_RED, label, 8, signal=signal, data=data)
        self._latch = val_latch
        self._assert = val_assert
        

    def clock_write(self, event):
        if isinstance(event, ClockPulse) and event.state == 1:
            if self._signals.read_signal(self._assert):
                self._data.assert_value(self._cur_value)
                return
            
            
    def clock_read(self, event):
        if isinstance(event, ClockPulse) and event.state == 1:
            if self._signals.read_signal(self._latch):
                self.assert_value(self._data.read_value())
                return
            

    def read_value(self):
        return self._cur_value
