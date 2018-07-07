import const
from component import Component
from eventtypes import ClockPulse

class InstDecode(Component):

    signals = {
        'HLT' : 0b1000000000000000, # Halt
        'MI'  : 0b0100000000000000, # Memory Address Register In
        'RI'  : 0b0010000000000000, # RAM In
        'RO'  : 0b0001000000000000, # RAM Out
        'IO'  : 0b0000100000000000, # Instruction Out
        'II'  : 0b0000010000000000, # Instruction In
        'AI'  : 0b0000001000000000, # A Register In
        'AO'  : 0b0000000100000000, # A Register Out
        'BI'  : 0b0000000010000000, # B Register In
        'BO'  : 0b0000000001000000, # B Register Out
        'EO'  : 0b0000000000100000, # Sum Out
        'SU'  : 0b0000000000010000, # Subtract
        'OI'  : 0b0000000000001000, # Output In
        'CE'  : 0b0000000000000100, # Program Counter Enable
        'CO'  : 0b0000000000000010, # Program Counter Out
        'J'   : 0b0000000000000001  # Jump
    }


    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_YELLOW, "Instruction Decoder", 16)
        self.assert_value(0)

        self._mode = 0

        keys = list(InstDecode.signals)
        for i in range(self._bit_width):
            key = keys[i]
            for j in range(len(key)):
                self._window.addstr(3+j, 2+i*2, key[j])


    def reset(self):
        self.assert_value(0)
        self._mode = 0


    def receive_clock(self, event):
        if isinstance(event, ClockPulse):
            # self.assert_value(0)
            if self._mode == 0:
                self.assert_value(InstDecode.signals['CE'])
                self._mode = 1
            elif self._mode == 1:
                self.assert_value(InstDecode.signals['CO'] | InstDecode.signals['AI'])
                self._mode = 2
            elif self._mode == 2:
                self.assert_value(InstDecode.signals['AO'] | InstDecode.signals['BI'])
                self._mode = 3
            elif self._mode == 3:
                self.assert_value(InstDecode.signals['EO'] | InstDecode.signals['OI'])
                self._mode = 0

    def enable_signal(self, signal):
        self.assert_value(self._cur_value | InstDecode.signals[signal])


    def read_signal(self, signal):
        return self._cur_value & InstDecode.signals[signal]
