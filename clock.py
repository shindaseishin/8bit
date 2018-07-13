from threading import Timer
import zope.event

from component import Component
from eventtypes import ClockPulse
import const

class Clock(Component):

    def __init__(self, window, decode=None):
        self._pause = True
        self._halt = False
        self._cycle = const.CLOCK_CYCLE
        self._thread = None
        self._inst_decode = decode
        super().__init__(window, const.COLOR_PAIR_BLUE, "Clock", 1)
        self.latch_value(1)

    def __del__(self):
        self._thread.cancel()


    def display(self):
        super().display()
        if self._halt == True:
            self._window.addstr(4, 2, "Halted")
        elif self._pause == True:
            self._window.addstr(4, 2, "Paused")
        else:
            self._window.addstr(4, 2, "      ")

        hrz = round(1.0 / self._cycle / 2,  3)
        self._window.addstr(2, 6, "Hz: {:4.3f}".format(hrz))
        self._window.refresh()


    def pulse(self, window):
        self.latch_value(1 - self._cur_value)
        self.display()
        self._inst_decode.pulse()
        self.start()


    def start(self):
        if self._halt != True:
            self._thread = Timer(self._cycle, self.pulse, [self._window])
            self._thread.start()


    def pause_toggle(self):
        self._pause = not self._pause
        if not self._pause:
            self._thread.cancel()
        else:
            self.start()


    def change_speed(self,  direction):
        self._cycle += direction * const.CLOCK_CYCLE_DELTA


    def halt(self):
        self._halt = True
        self._thread.cancel()
        self.display()


    def manual_pulse(self):
        if not self._halt and self._pause:
            self.latch_value(1 - self._cur_value)
            self._inst_decode.pulse()


    def reset(self):
        self._thread.cancel()
        self._halt = False
        self._pause = True;
        self.latch_value(1)
        self.start()
