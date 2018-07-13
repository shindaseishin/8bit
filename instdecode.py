import curses

import const
from component import Component
from eventtypes import ClockPulse
from microcode import microcode

class InstDecode(Component):
    def __init__(self, window, components):
        self._components = components
        self._latched_instruction = components['mem'].read_ram(0)
        self._step = 0
        super().__init__(window, const.COLOR_PAIR_YELLOW, "Instruction Decoder", 16)

        # Display flag names below the LED
        keys = list(const.SIGNALS)
        for i in range(self._bit_width):
            key = keys[i]
            for j in range(len(key)):
                self._window.addstr(3+j, 2+i*2, key[j])


    def display(self):
        self._window.addstr(7, 2, self.decode_binary(value=self._latched_instruction), curses.color_pair(const.COLOR_PAIR_RED) | curses.A_BOLD)
        super().display()


    def refresh(self):
        for c in self._components:
            self._components[c].display()
        self.display()

    def pulse(self):
        self.latch_value(0)

        instruction = self._latched_instruction << 8 | self._step

        keys = list(const.SIGNALS)
        for i in keys:
            mc = microcode[instruction]>>7
            if bool(mc & const.SIGNALS[i]):
                self.enable_signal(i)

        self._step = (self._step + 1) & 0b11
        self.refresh()



    def reset(self):
        for c in self._components:
            self._components[c].reset()
        self.latch_value(0)
        self._latched_address = 0
        self._step = 0


    def enable_signal(self, signal):
        self.latch_value(self._cur_value | const.SIGNALS[signal])


    def read_signal(self, signal):
        return self._cur_value | const.SIGNALS[signal]


    def latch_instruction(self, value):
        self._latched_instruction = value
