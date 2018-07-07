import curses
from curses import wrapper
import zope.event


import const
from component import Component
from databus import DataBus
from addrbus import AddrBus
from signalbus import SignalBus
from clock import Clock
from help import Help
from output import Output
from programcounter import ProgramCounter
from register import Register


def interface(stdscr):
    curses.noecho()
    curses.curs_set(0)
    stdscr.clear
    stdscr.refresh()
    stdscr.nodelay(True)

    curses.init_pair(const.COLOR_PAIR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_BLUE, curses.COLOR_CYAN, curses.COLOR_BLACK)

    row_height = (curses.LINES - 1) // 5
    col_width  = (curses.COLS - 1) // 4

    data_bus = DataBus(curses.newwin(row_height * 1, col_width * 2, row_height * 4, col_width * 0))
    addr_bus = AddrBus(curses.newwin(row_height * 1, col_width * 2, row_height * 3, col_width * 0))
    sgnl_bus = SignalBus(curses.newwin(row_height * 1, col_width * 2, row_height * 2, col_width * 0))

    clock    = Clock(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 3), signal=sgnl_bus)
    prog_cnt = ProgramCounter(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 2), signal=sgnl_bus, data=data_bus)

    mem      = Component(curses.newwin(row_height * 2, col_width * 1, row_height * 0, col_width * 0), const.COLOR_PAIR_RED,    'Memory',               11)

    reg_a    = Register(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 1), 'Register A', 'AI', 'AO', signal=sgnl_bus, data=data_bus)
    alu      = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 2), const.COLOR_PAIR_RED,    'ALU',                   8)
    reg_b    = Register(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 3), 'Register B', 'BI', 'BO', signal=sgnl_bus, data=data_bus)
    inst_reg = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 1), const.COLOR_PAIR_GREEN,  'Instruction Register', 16)

    output   = Output(curses.newwin(row_height * 1, col_width * 2, row_height * 3, col_width * 2), signal=sgnl_bus, data=data_bus)
    control  = Component(curses.newwin(row_height * 1, col_width * 2, row_height * 2, col_width * 2), const.COLOR_PAIR_YELLOW, 'Control Logic',        24)

    help     = Help(curses.newwin(row_height * 1, col_width * 2, row_height * 4, col_width * 2))

    zope.event.subscribers.append(sgnl_bus.receive_clock)
    zope.event.subscribers.append(prog_cnt.receive_clock)
    zope.event.subscribers.append(output.receive_clock)

    clock.start_clock();

    if curses.has_colors():
        quit = False
        while quit == False:
            c = stdscr.getch()
            if c == ord('q') or c == ord('Q'):
                quit = True
            elif c == ord('p') or c == ord('P'):
                clock.pause_toggle()
            elif c == ord('h') or c == ord('H'):
                # clock.halt()
                sgnl_bus.enable_signal('HLT')
            elif c == ord('a') or c == ord('A'):
                clock.change_speed(-1)
            elif c == ord('z') or c == ord('Z'):
                clock.change_speed(1)
            elif c == ord('o') or c == ord('O'):
                clock.manual_pulse()
            elif c == ord('r') or c == ord('R'):
                sgnl_bus.reset()
                clock.reset()
                prog_cnt.reset()
                output.reset()
    else:
        stdscr.addstr(0, 0, "Color support required. Press any key to exit")

    clock.halt()

    curses.echo()
    curses.endwin()
    stdscr = None


if __name__ == "__main__":
    wrapper(interface)
