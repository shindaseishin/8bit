import curses

LED_OFF = u"\u25EF "
LED_ON  = u"\u25C9 "

COLOR_PAIR_WHITE  = curses.COLOR_WHITE
COLOR_PAIR_RED    = curses.COLOR_RED
COLOR_PAIR_GREEN  = curses.COLOR_GREEN
COLOR_PAIR_YELLOW = curses.COLOR_YELLOW
COLOR_PAIR_BLUE   = curses.COLOR_BLUE

CLOCK_CYCLE = 0.1
CLOCK_CYCLE_DELTA = 0.01

SIGNALS = {
    'HLT' : 0b10000000000000000, # Halt
    'MI'  : 0b01000000000000000, # Memory Address Register In
    'RI'  : 0b00100000000000000, # RAM In
    'ROA' : 0b00010000000000000, # RAM Out Address
    'ROD' : 0b00001000000000000, # RAM Out Address
    'AI'  : 0b00000100000000000, # A Register In
    'AO'  : 0b00000010000000000, # A Register Out
    'BI'  : 0b00000001000000000, # B Register In
    'BO'  : 0b00000000100000000, # B Register Out
    'EO'  : 0b00000000010000000, # Sum Out
    'SU'  : 0b00000000001000000, # Subtract
    'OI'  : 0b00000000000100000, # Output In
    'CE'  : 0b00000000000010000, # Program Counter Enable
    'CO'  : 0b00000000000001000, # Program Counter Out
    'J'   : 0b00000000000000100, # Jump
    'II'  : 0b00000000000000010, # Instruction In
    'RN'  : 0b00000000000000001, # Increment Address         
}
