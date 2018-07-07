import const
from bus import Bus
from eventtypes import ClockPulse

class SignalBus(Bus):

    signals = {
        'HLT' : 0b100000000000000000, # Halt
        'MI'  : 0b010000000000000000, # Memory Address Register In
        'RI'  : 0b001000000000000000, # RAM In
        'RO'  : 0b000100000000000000, # RAM Out
        'IO'  : 0b000010000000000000, # Instruction Out
        'II'  : 0b000001000000000000, # Instruction In
        'AI'  : 0b000000100000000000, # A Register In
        'AO'  : 0b000000010000000000, # A Register Out
        'BI'  : 0b000000001000000000, # B Register In
        'BO'  : 0b000000000100000000, # B Register Out
        'EO'  : 0b000000000010000000, # Sum Out
        'SU'  : 0b000000000001000000, # Subtract
        'OI'  : 0b000000000000100000, # Output In
        'CE'  : 0b000000000000010000, # Program Counter Enable
        'CO'  : 0b000000000000001000, # Program Counter Out
        'J'   : 0b000000000000000100, # Jump
        'JZ'  : 0b000000000000000010, # Jump Zero
        'JC'  : 0b000000000000000001  # Jump Carry
    }


    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_YELLOW, "Signal Bus", 18)
        self.assert_value(0)

        self._mode = 0

        keys = list(SignalBus.signals)
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
                self.assert_value(SignalBus.signals['CE'])
                self._mode = 1
            elif self._mode == 1:
                self.assert_value(SignalBus.signals['CO'] | SignalBus.signals['AI'])
                self._mode = 2
            elif self._mode == 2:
                self.assert_value(SignalBus.signals['AO'] | SignalBus.signals['BI'])
                self._mode = 3
            elif self._mode == 3:
                self.assert_value(SignalBus.signals['BO'] | SignalBus.signals['OI'])
                self._mode = 0

    def enable_signal(self, signal):
        self.assert_value(self._cur_value | SignalBus.signals[signal])


    def read_signal(self, signal):
        return self._cur_value & SignalBus.signals[signal]
