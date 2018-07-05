from bus import Bus
import const

class AddrBus(Bus):

    def __init__(self, window):
        Bus.__init__(self, window, const.COLOR_PAIR_GREEN, "Address Bus", 16)
