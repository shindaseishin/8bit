import curses
from curses import wrapper

import const
from databus import DataBus
from addrbus import AddrBus
from instdecode import InstDecode
from clock import Clock
from help import Help
from output import Output
from programcounter import ProgramCounter
from register import Register
from alu import Alu
from memory import Memory


def interface(stdscr):
    curses.noecho()
    curses.curs_set(0)
    stdscr.clear
    stdscr.refresh()
    stdscr.nodelay(True)

    if not curses.has_colors():
        print("Color support required. Press any key to exit")
        curses.echo()
        curses.endwin()
        stdscr = None

    curses.init_pair(const.COLOR_PAIR_WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_BLUE, curses.COLOR_CYAN, curses.COLOR_BLACK)

    row_height = (curses.LINES - 1) // 4
    col_width  = (curses.COLS - 1) // 4

    components = {
        'data_bus': DataBus(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 0)),
        'addr_bus': AddrBus(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 0)),
        'prog_cnt': ProgramCounter(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 1)),
        'mem'     : Memory(curses.newwin(row_height * 2, col_width * 2, row_height * 2, col_width * 0)),
        'reg_a'   : Register(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 1), 'Register A'),
        'reg_b'   : Register(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 3), 'Register B'),
        'alu'     : Alu(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 2)),
        'output'  : Output(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 3)),
    }

    components['mem'].load_mem_from_file('dump.ram')

    help     = Help(curses.newwin(row_height * 1, col_width * 2, row_height * 3, col_width * 2))
    inst_dec = InstDecode(curses.newwin(row_height * 1, col_width * 2, row_height * 2, col_width * 2), components)
    clock    = Clock(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 2), decode=inst_dec)

    inst_dec.refresh()

    # clock.start()

    quit = False
    while quit == False:
        c = stdscr.getch()
        if c == ord('q') or c == ord('Q'):
            quit = True
        elif c == ord('p') or c == ord('P'):
            clock.pause_toggle()
        elif c == ord('h') or c == ord('H'):
            clock.halt()
        elif c == ord('a') or c == ord('A'):
            clock.change_speed(-1)
        elif c == ord('z') or c == ord('Z'):
            clock.change_speed(1)
        elif c == ord('o') or c == ord('O'):
            clock.manual_pulse()
        elif c == curses.KEY_UP:
            components['mem'].scroll_up()
        elif c == curses.KEY_DOWN:
            components['mem'].scroll_down()
        elif c == ord('r') or c == ord('R'):
            clock.reset()
            inst_dec.reset()


    clock.halt()

    curses.echo()
    curses.endwin()
    stdscr = None


if __name__ == "__main__":
    wrapper(interface)
