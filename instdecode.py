import const
from component import Component
from eventtypes import ClockPulse

class InstDecode(Component):

    signals = {
        'HLT' : 0b10000000000000, # Halt
        'MI'  : 0b01000000000000, # Memory Address Register In
        'RI'  : 0b00100000000000, # RAM In
        'RO'  : 0b00010000000000, # RAM Out
        'AI'  : 0b00001000000000, # A Register In
        'AO'  : 0b00000100000000, # A Register Out
        'BI'  : 0b00000010000000, # B Register In
        'BO'  : 0b00000001000000, # B Register Out
        'EO'  : 0b00000000100000, # Sum Out
        'SU'  : 0b00000000010000, # Subtract
        'OI'  : 0b00000000001000, # Output In
        'CE'  : 0b00000000000100, # Program Counter Enable
        'CO'  : 0b00000000000010, # Program Counter Out
        'J'   : 0b00000000000001  # Jump
    }


    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_YELLOW, "Instruction Decoder", 14)
        self.assert_value(0)

        self._step = 0

        keys = list(InstDecode.signals)
        for i in range(self._bit_width):
            key = keys[i]
            for j in range(len(key)):
                self._window.addstr(3+j, 2+i*2, key[j])


    def reset(self):
        self.assert_value(0)
        self._mode = 0


    def decode_instruction(self,  event):
        if isinstance(event, ClockPulse):
            self.assert_value(0)
            if self._step == 0:
                self.enable_signal('CO')
                self.enable_signal('MI')
            elif self._step == 1:
                self.enable_signal('RO')
                self.enable_signal('AI')
            elif self._step == 2:
                self.enable_signal('CE')
            elif self._step == 3:
                self.enable_signal('CO')
                self.enable_signal('MI')
            elif self._step == 4:
                self.enable_signal('RO')
                self.enable_signal('BI')
            elif self._step == 5:
                self.enable_signal('EO')
                self.enable_signal('OI')
                self._step = -1
        self._step = (self._step + 1) & 0b111


    def enable_signal(self, signal):
        self.assert_value(self._cur_value | InstDecode.signals[signal])


    def read_signal(self, signal):
        return self._cur_value & InstDecode.signals[signal]
