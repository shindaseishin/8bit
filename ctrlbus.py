import const
from bus import Bus

class CtrlBus(Bus):

    def __init__(self, window, label, bit_width):
        Bus.__init__(self, window, const.COLOR_PAIR_YELLOW, label, bit_width)
