from bus import Bus

import const

class DataBus(Bus):

    def __init__(self, window, label, bit_width):
        Bus.__init__(self, window, const.COLOR_PAIR_RED, label, bit_width)
