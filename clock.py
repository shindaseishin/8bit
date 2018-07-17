from threading import Timer

from component import Component
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
        self.stop()


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


    def pulse(self, restart=True):
        self.latch_value(1 - self._cur_value)
        if self._cur_value == 1:
            hlt = self._inst_decode.clock_high()
            if hlt:
                self.halt()
        else:
            self._inst_decode.clock_low()
        self.display()

        if restart:
            self.start()


    def manual_pulse(self):
        if not self._halt and self._pause:
            self.pulse(restart=False)


    def start(self):
        if not self._halt:
            self.stop()
            self._thread = Timer(self._cycle, self.pulse, [])
            self._thread.start()


    def stop(self):
        if self._thread != None:
            self._thread.cancel()
            self._thread = None


    def pause_toggle(self):
        self._pause = not self._pause
        if self._pause:
            self.stop()
        else:
            self.start()


    def change_speed(self,  direction):
        self._cycle += direction * const.CLOCK_CYCLE_DELTA


    def halt(self):
        self.stop()
        self._halt = True
        self.display()


    def reset(self):
        self.stop()
        self._halt = False
        self._pause = True;
        self.latch_value(1)
        self.display()
