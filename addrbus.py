from bus import Bus
import const

class AddrBus(Bus):

    def __init__(self, window, label, bit_width):
        Bus.__init__(self, window, const.COLOR_PAIR_GREEN, label, bit_width)
