from component import Component
import const

class Memory(Component):
    def __init__(self, window, signal=None, data=None, address=None):
        self._ram = [42] * 2**11
        self._dump_top = 0
        super().__init__(window, const.COLOR_PAIR_RED, "Memory", 8)
        for i in range(2048):
            self._ram[i] = i & self._bit_mask 

    def display(self):
        super().display()
        height = self._window.getmaxyx()[0] - 7
    
        for i in range(self._dump_top, self._dump_top + height):
            line = i * 16
            if i < 2048//16:
                self._window.addstr(4+i-self._dump_top, 2,  "{:04d}:".format(line))
                for j in range(16):
                    self._window.addstr(4+i-self._dump_top, 8 + j*3,  "{:02x} ".format(self._ram[i+j]))
            self._window.refresh()

    
    def scroll_up(self):
        delta = self._window.getmaxyx()[0] - 7
        if self._dump_top - delta < 0:
            self._dump_top = 0
        else:
            self._dump_top -= delta
        
        
    def scroll_down(self):
        delta = self._window.getmaxyx()[0] - 7
        last_line = 2048//16
        
        if self._dump_top + delta >= last_line:
            self._dump_top = last_line - delta
        else:
            self._dump_top += delta
            

    def receive_clock(self, event):
        self.display()
