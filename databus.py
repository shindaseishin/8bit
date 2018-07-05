from bus import Bus

import const

class DataBus(Bus):

    def __init__(self, window):
        Bus.__init__(self, window, const.COLOR_PAIR_RED, "Data Bus", 8)
