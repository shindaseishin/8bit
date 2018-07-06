import const
from bus import Bus

class CtrlBus(Bus):

    def __init__(self, window):
        Bus.__init__(self, window, const.COLOR_PAIR_YELLOW, "Control Bus", 24)
