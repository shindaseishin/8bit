from component import Component

import const

class Alu(Component):
    OPERATION_ADD = 1
    OPERATION_SUB = -1

    def __init__(self, window):
        self._carry = False
        super().__init__(window, const.COLOR_PAIR_RED, 'ALU', 8)


    def operate(self, a, b, operation):
        b = b * operation

        value = a + b
        if (operation == Alu.OPERATION_ADD and value > 255) or (operation == Alu.OPERATION_SUB and value < 0):
            self._carry = True
        else :
            self._carry = False

        self.latch_value(value)


    def read_carry(self):
        return self._carry
        
