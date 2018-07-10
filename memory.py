import curses

from component import Component
from eventtypes import ClockPulse
import const

class Memory(Component):
    def __init__(self, window, signal=None, data=None, address=None):
        self._ram = bytearray([42]*256)
        self._dump_top = 0
        self._latched_address = 0
        super().__init__(window, const.COLOR_PAIR_RED, "Memory", 8,  signal=signal,  data=data,  address=address)

    def display(self):
        super().display()
        height = self._window.getmaxyx()[0] - 7

        for i in range(self._dump_top, self._dump_top + height):
            line = i * 16
            if i < 256//16:
                self._window.addstr(4+i-self._dump_top, 2,  "{:04d}:".format(line))
                for j in range(16):
                    colour = const.COLOR_PAIR_WHITE
                    if (i*16+j) == self._latched_address:
                        colour = const.COLOR_PAIR_GREEN
                    self._window.addstr(4+i-self._dump_top, 8 + j*3,  "{:02x} ".format(self._ram[i*16+j]), curses.color_pair(colour))
            self._window.refresh()


    def scroll_up(self):
        delta = self._window.getmaxyx()[0] - 7
        if self._dump_top - delta < 0:
            self._dump_top = 0
        else:
            self._dump_top -= delta


    def scroll_down(self):
        delta = self._window.getmaxyx()[0] - 7
        last_line = 256//16

        if self._dump_top + delta >= last_line:
            self._dump_top = last_line - delta
        else:
            self._dump_top += delta


    def clock_write(self, event):
        if isinstance(event, ClockPulse) and event.state == 1:
            if self._signals.read_signal('RO'):
                self._data.assert_value(self._ram[self._latched_address])
            if self._signals.read_signal('II'):
                self._signals.latch_instruction(self._ram[self._latched_address])


    def clock_read(self, event):
        if isinstance(event, ClockPulse) and event.state == 1:
            if self._signals.read_signal('RI'):
                self._ram[self._latched_address] = self._data.read_value()
            if self._signals.read_signal('MI'):
                self._latched_address = self._address.read_value()
                self._cur_value = self._ram[self._latched_address]
            if self._signals.read_signal('RN'):
                self._latched_address = self._address.read_value()+1
                self._address.assert_value(self._latched_address)
                self._cur_value = self._ram[self._latched_address]
            self.display()


    def load_mem_from_file(self, filename):
        with open(filename, "rb") as f:
             self._ram = f.read(256)
