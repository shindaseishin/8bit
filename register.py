from component import Component
import const

class Register(Component):
    def __init__(self, window, label):
        super().__init__(window, const.COLOR_PAIR_RED, label, 8)
