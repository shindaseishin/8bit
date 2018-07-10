import curses

import const
from component import Component
from eventtypes import ClockPulse
from microcode import microcode

class InstDecode(Component):

    signals = {
        'HLT' : 0b10000000000000000, # Halt
        'MI'  : 0b01000000000000000, # Memory Address Register In
        'RI'  : 0b00100000000000000, # RAM In
        'RO'  : 0b00010000000000000, # RAM Out
        'AI'  : 0b00001000000000000, # A Register In
        'AO'  : 0b00000100000000000, # A Register Out
        'BI'  : 0b00000010000000000, # B Register In
        'BO'  : 0b00000001000000000, # B Register Out
        'EO'  : 0b00000000100000000, # Sum Out
        'SU'  : 0b00000000010000000, # Subtract
        'OI'  : 0b00000000001000000, # Output In
        'CE'  : 0b00000000000100000, # Program Counter Enable
        'CO'  : 0b00000000000010000, # Program Counter Out
        'J'   : 0b00000000000001000, # Jump
        'II'  : 0b00000000000000100, # Instruction In
        'RN'  : 0b00000000000000010, # Increment Address
        'PSS' : 0b00000000000000001  # Pass to next instruction
    }


    def __init__(self, window, data=None, address=None):
        self._latched_instruction = 0

        super().__init__(window, const.COLOR_PAIR_YELLOW, "Instruction Decoder", 17, data=data, address=address)
        self.assert_value(0)

        self._step = 0

        # Display flag names below the LED for that signal
        keys = list(InstDecode.signals)
        for i in range(self._bit_width):
            key = keys[i]
            for j in range(len(key)):
                self._window.addstr(3+j, 2+i*2, key[j])


    def display(self):
        self._window.addstr(7, 2, self.decode_binary(value=self._latched_instruction), curses.color_pair(const.COLOR_PAIR_RED) | curses.A_BOLD)
        super().display()


    def reset(self):
        self.assert_value(0)
        self._latched_address = 0
        self._step = 0


    def receive_clock(self,  event):
        if isinstance(event, ClockPulse) and event.state == 0:
            self.assert_value(0)

            instruction = self._latched_instruction << 8 | self._step

            keys = list(InstDecode.signals)
            for i in keys:
                mc = microcode[instruction]>>7
                if bool(mc & InstDecode.signals[i]):
                    self.enable_signal(i)

            self._step = (self._step + 1) & 0b111
            if self.read_signal('PSS'):
                self._step = 0


    def enable_signal(self, signal):
        self.assert_value(self._cur_value | InstDecode.signals[signal])


    def read_signal(self, signal):
        return self._cur_value & InstDecode.signals[signal]


    def latch_instruction(self, value):
        self._latched_instruction = value
