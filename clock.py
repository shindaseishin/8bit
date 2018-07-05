from threading import Timer

from component import Component
import const

class Clock(Component):

    def __init__(self, window, cycle):
        self._pause = False
        self._halt = False
        self._cycle = cycle
        self._thread = None
        super().__init__(window, const.COLOR_PAIR_BLUE, "Clock", 1)


    def __del__(self):
        self._thread.cancel()


    def display(self):
        Component.display(self)
        if self._halt == True:
            self._window.addstr(3, 2, "Halted")
        elif self._pause == True:
            self._window.addstr(3, 2, "Paused")
        else:
            self._window.addstr(3, 2, "      ")
        self._window.refresh()


    def pulse(self, window):
        if self._pause == True or self._halt == True:
            pass # NoOp, machine is in a non-executing state
        else:
            self._cur_value = 1 - self._cur_value
            self.display()
        self.start_clock()


    def start_clock(self):
        if self._halt != True:
            self._thread = Timer(self._cycle, self.pulse, [self._window])
            self._thread.start()


    def pause_toggle(self):
        self._pause = not self._pause
        self.display()


    def halt(self):
        self._halt = True
        self._thread.cancel()
        self.display()


    def reset(self):
        self._thread.cancel()
        self._halt = False
        self._pause = False;
        self._cur_value = 0
        self.display()
        self.start_clock()
