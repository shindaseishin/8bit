from bus import Bus

import const

class DataBus(Bus):

    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_RED, "Data Bus", 8)
