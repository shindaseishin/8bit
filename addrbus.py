from bus import Bus
import const

class AddrBus(Bus):

    def __init__(self, window):
        super().__init__(window, const.COLOR_PAIR_GREEN, "Address Bus", 11)
