import curses
from curses import wrapper


import const
from component import Component
from databus import DataBus
from addrbus import AddrBus
from ctrlbus import CtrlBus


def interface(stdscr):
    curses.noecho()
    stdscr.clear
    stdscr.refresh()
    stdscr.nodelay(True)

    curses.init_pair(const.COLOR_PAIR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_BLUE, curses.COLOR_CYAN, curses.COLOR_BLACK)

    row_height = (curses.LINES - 1) // 6
    col_width  = (curses.COLS - 1) // 4

    data_bus = DataBus(curses.newwin(row_height * 1, col_width * 4, row_height * 4, col_width * 0), 'Data Bus',             16)
    addr_bus = AddrBus(curses.newwin(row_height * 1, col_width * 4, row_height * 3, col_width * 0), 'Address Bus',          16)
    ctrl_bus = CtrlBus(curses.newwin(row_height * 1, col_width * 4, row_height * 2, col_width * 0), 'Control Bus',          24)

    clock    = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 3), const.COLOR_PAIR_BLUE,   'Clock',                 1)
    prog_cnt = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 2), const.COLOR_PAIR_BLUE,   'Program Counter',       8)

    mem      = Component(curses.newwin(row_height * 2, col_width * 1, row_height * 0, col_width * 0), const.COLOR_PAIR_RED,    'Memory',               11)

    reg_a    = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 1), const.COLOR_PAIR_RED,    'Register A',            8)
    alu      = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 2), const.COLOR_PAIR_RED,    'ALU',                   8)
    reg_b    = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 3), const.COLOR_PAIR_RED,    'Register B',            8)
    inst_reg = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 1), const.COLOR_PAIR_GREEN,  'Instruction Register', 16)

    output   = Component(curses.newwin(row_height * 1, col_width * 2, row_height * 5, col_width * 2), const.COLOR_PAIR_RED,    'Output',                8)
    control  = Component(curses.newwin(row_height * 1, col_width * 2, row_height * 5, col_width * 0), const.COLOR_PAIR_YELLOW, 'Control Logic',        24)

    stdscr.addstr(curses.LINES-1, 0, "[q] Quit ")
    if curses.has_colors():
        quit = False
        while quit == False:
            c = stdscr.getch()
            if c == ord('q'):
                quit = True

    else:
        stdscr.addstr(0, 0, "Color support required. Press any key to exit")

    curses.echo()
    curses.endwin()
    stdscr = None

if __name__ == "__main__":
    wrapper(interface)
