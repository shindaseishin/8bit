from threading import Timer
import zope.event

from component import Component
from eventtypes import ClockPulse
import const

class Clock(Component):

    def __init__(self, window, signal=None):
        self._pause = False
        self._halt = False
        self._cycle = const.CLOCK_CYCLE
        self._thread = None
        super().__init__(window, const.COLOR_PAIR_BLUE, "Clock", 1, signal=signal)


    def __del__(self):
        self._thread.cancel()


    def display(self):
        Component.display(self)
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
        if self._signals.read_signal('HLT'):
            self.halt()

        if self._pause == True or self._halt == True:
            pass # NoOp, machine is in a non-executing state
        else:
            self.assert_value(1 - self._cur_value)
            self.display()
            if self._cur_value == 1:
                zope.event.notify(ClockPulse())
        self.start_clock()


    def start_clock(self):
        if self._halt != True:
            self._thread = Timer(self._cycle, self.pulse, [self._window])
            self._thread.start()


    def pause_toggle(self):
        self._pause = not self._pause
        self.display()


    def change_speed(self,  direction):
        self._cycle += direction * const.CLOCK_CYCLE_DELTA


    def halt(self):
        self._halt = True
        self._thread.cancel()
        self.display()


    def manual_pulse(self):
        if not self._halt and self._pause:
            zope.event.notify(ClockPulse())


    def reset(self):
        self._thread.cancel()
        self._halt = False
        self._pause = True;
        self.assert_value(0)
        self.start_clock()
