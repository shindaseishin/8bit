import curses

from eventtypes import ClockPulse
from component import Component
import const

class ProgramCounter(Component):
    def __init__(self, window, signal=None, data=None):
        super().__init__(window, const.COLOR_PAIR_BLUE, 'Program Counter', 8, signal=signal, data=data)

    def receive_clock(self, event):
        if self._signals.read_signal('CE'):
            self.assert_value(self._cur_value + 1)
            return

        if self._signals.read_signal('CO'):
            self._data.assert_value(self._cur_value)
            return
