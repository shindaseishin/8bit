from component import Component
import const

class ProgramCounter(Component):
    def __init__(self, window, signal=None, data=None, address=None):
        super().__init__(window, const.COLOR_PAIR_BLUE, 'Program Counter', 11, signal=signal, data=data,  address=address)

    def clock_write(self, event):
        if self._signals.read_signal('CO'):
            #self._data.assert_value(self._cur_value)
            self._address.assert_value(self._cur_value)
            return


    def clock_read(self, event):
        if self._signals.read_signal('CE'):
            self.assert_value(self._cur_value + 1)
            return

