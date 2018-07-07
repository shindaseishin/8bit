from component import Component
import const

class Memory(Component):
    def __init__(self, window, signal=None, data=None, address=None):
        self._ram = [42] * 2**11
        self._dump_top = 0
        super().__init__(window, const.COLOR_PAIR_RED, "Memory", 8)

    def display(self):
        super().display()
        height = self._window.getmaxyx()[0] - 7
        
        for i in range(self._dump_top, self._dump_top + height):
            line = i * 16
            if i < 2048:
                self._window.addstr(4+i, 2,  "{:03d}:".format(line))
                for j in range(16):
                    self._window.addstr(4+i, 7 + j*3,  "{:02x} ".format(self._ram[i*16+j]))
            self._window.refresh()


    def receive_clock(self, event):
       # self.assert_value(self._address.read_value())
       pass 
