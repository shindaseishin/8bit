import curses

import const
from component import Component
from alu import Alu
from microcode import microcode

class InstDecode(Component):
    def __init__(self, window, components):
        self._components = components
        self._latched_instruction = self._components['mem'].read_ram(0)
        self._step = 0
        super().__init__(window, const.COLOR_PAIR_YELLOW, "Instruction Decoder", len(const.SIGNALS))

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

    # Decode instructions and set control lines on clock low
    def clock_low(self):
        self.latch_value(0)

        instruction = self._latched_instruction << 8 | self._step
        self.refresh()
        mc = microcode[instruction]

        keys = list(const.SIGNALS)
        for i in keys:
            if bool(mc & const.SIGNALS[i]):
                self.enable_signal(i)
        self.refresh()


    def clock_high(self):
        retval = False

        if self.read_signal('HLT'):
            retval = True

        if self.read_signal('CE'):
            self._components['prog_cnt'].step()

        # Put data on the busses
        if self.read_signal('CO'):
            self._components['addr_bus'].latch_value(self._components['prog_cnt'].read_value())
        if self.read_signal('ROA'):
            self._components['addr_bus'].latch_value(self._components['mem'].read_value())
        if self.read_signal('ROD'):
            self._components['data_bus'].latch_value(self._components['mem'].read_value())
        if self.read_signal('AO'):
            self._components['data_bus'].latch_value(self._components['reg_a'].read_value())
        if self.read_signal('BO'):
            self._components['data_bus'].latch_value(self._components['reg_b'].read_value())
        if self.read_signal('EO'):
            self._components['data_bus'].latch_value(self._components['alu'].read_value())

        if self.read_signal('MI'):
            self._components['mem'].latch_address(self._components['addr_bus'].read_value())
        if self.read_signal('RI'):
            self._components['mem'].set_ram(self._components['data_bus'].read_value())

        if self.read_signal('AI'):
            self._components['reg_a'].latch_value(self._components['data_bus'].read_value())
        if self.read_signal('BI'):
            self._components['reg_b'].latch_value(self._components['data_bus'].read_value())

        if self.read_signal('EE'):
            if self.read_signal('SU'):
                self._components['alu'].operate(self._components['reg_a'].read_value(), self._components['reg_b'].read_value(), Alu.OPERATION_SUB)
            else:
                self._components['alu'].operate(self._components['reg_a'].read_value(), self._components['reg_b'].read_value(), Alu.OPERATION_ADD)

        if self.read_signal('J'):
            self._components['prog_cnt'].latch_value(self._components['addr_bus'].read_value())
        if self.read_signal('JZ') and self._components['alu'].read_value() == 0x00:
            self._components['prog_cnt'].latch_value(self._components['addr_bus'].read_value())
        if self.read_signal('JO') and self._components['alu'].read_carry():
            self._components['prog_cnt'].latch_value(self._components['addr_bus'].read_value())

        if self.read_signal('OI'):
            self._components['output'].latch_value(self._components['data_bus'].read_value())
        if self.read_signal('II'):
            self.latch_instruction(self._components['mem'].read_value())

        if self.read_signal('RN'):
            self._components['mem'].operand()

        if self.read_signal('HLT'):
            self._step = 0x00
        else:
            self._step = (self._step + 1) & 0b11

        self.refresh()
        return retval


    def reset(self):
        for c in self._components:
            self._components[c].reset()
        self.latch_value(0)
        self._latched_address = 0
        self._step = 0
        self.refresh()


    def enable_signal(self, signal):
        self.latch_value(self._cur_value | const.SIGNALS[signal])


    def read_signal(self, signal):
        return (bool)(self._cur_value & const.SIGNALS[signal])


    def latch_instruction(self, value):
        self._latched_instruction = value
