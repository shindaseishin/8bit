import curses

from component import Component
import const

class Memory(Component):
    def __init__(self, window):
        self._ram = bytearray([42]*256)
        self._dump_top = 0
        self._latched_address = 0
        super().__init__(window, const.COLOR_PAIR_RED, "Memory", 8)

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


    def read_ram(self, address):
        return self._ram[address]


    def set_ram(self, value):
        self._ram[self._latched_address] = value


    def latch_address(self, address):
        self._latched_address = address
        self.latch_value(self._ram[self._latched_address])


    def operand(self):
        self.latch_address(self._latched_address + 1)


    def load_mem_from_file(self, filename):
        with open(filename, "rb") as f:
            data = bytearray(f.read(256))
            for i in range(len(data), 256):
                data.append(0x00)
            self._ram = data
