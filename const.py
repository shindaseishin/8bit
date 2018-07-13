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
    'HLT' : 0b1000000000000000, # Halt                       - 0x08000
    'MI'  : 0b0100000000000000, # Memory Address Register In - 0x4000
    'RI'  : 0b0010000000000000, # RAM In                     - 0x2000
    'RO'  : 0b0001000000000000, # RAM Out                    - 0x1000
    'AI'  : 0b0000100000000000, # A Register In              - 0x0800
    'AO'  : 0b0000010000000000, # A Register Out             - 0x0400
    'BI'  : 0b0000001000000000, # B Register In              - 0x0200
    'BO'  : 0b0000000100000000, # B Register Out             - 0x0100
    'EO'  : 0b0000000010000000, # Sum Out                    - 0x0080
    'SU'  : 0b0000000001000000, # Subtract                   - 0x0040
    'OI'  : 0b0000000000100000, # Output In                  - 0x0020
    'CE'  : 0b0000000000010000, # Program Counter Enable     - 0x0010
    'CO'  : 0b0000000000001000, # Program Counter Out        - 0x0008
    'J'   : 0b0000000000000100, # Jump                       - 0x0004
    'II'  : 0b0000000000000010, # Instruction In             - 0x0002
    'RN'  : 0b0000000000000001, # Increment Address          - 0x0001
}
