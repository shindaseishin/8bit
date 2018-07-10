import curses
from curses import wrapper
import zope.event


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

    curses.init_pair(const.COLOR_PAIR_WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(const.COLOR_PAIR_BLUE, curses.COLOR_CYAN, curses.COLOR_BLACK)

    row_height = (curses.LINES - 1) // 4
    col_width  = (curses.COLS - 1) // 4

    data_bus = DataBus(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 0))
    addr_bus = AddrBus(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 0))
    inst_dec = InstDecode(curses.newwin(row_height * 1, col_width * 2, row_height * 2, col_width * 2), data=data_bus, address=addr_bus)

    clock    = Clock(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 2), signal=inst_dec)
    prog_cnt = ProgramCounter(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 1), signal=inst_dec, data=data_bus,  address=addr_bus)

    mem      = Memory(curses.newwin(row_height * 2, col_width * 2, row_height * 2, col_width * 0), signal=inst_dec, data=data_bus,  address=addr_bus)

    reg_a    = Register(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 1), 'Register A', 'AI', 'AO', signal=inst_dec, data=data_bus)
    reg_b    = Register(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 3), 'Register B', 'BI', 'BO', signal=inst_dec, data=data_bus)
    alu      = Alu(curses.newwin(row_height * 1, col_width * 1, row_height * 0, col_width * 2), reg_a, reg_b, signal=inst_dec, data=data_bus)

#    inst_reg = Component(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 1), const.COLOR_PAIR_GREEN,  'Instruction Register', 16)

    output   = Output(curses.newwin(row_height * 1, col_width * 1, row_height * 1, col_width * 3), signal=inst_dec, data=data_bus)
    Help(curses.newwin(row_height * 1, col_width * 2, row_height * 3, col_width * 2))

    mem.load_mem_from_file('dump.ram')

    zope.event.subscribers.append(inst_dec.receive_clock)

    zope.event.subscribers.append(prog_cnt.clock_write)
    zope.event.subscribers.append(mem.clock_write)
    zope.event.subscribers.append(reg_a.clock_write)
    zope.event.subscribers.append(reg_b.clock_write)
    zope.event.subscribers.append(alu.clock_write)
    zope.event.subscribers.append(output.clock_write)

    zope.event.subscribers.append(prog_cnt.clock_read)
    zope.event.subscribers.append(mem.clock_read)
    zope.event.subscribers.append(reg_a.clock_read)
    zope.event.subscribers.append(reg_b.clock_read)
    zope.event.subscribers.append(alu.clock_read)
    zope.event.subscribers.append(output.clock_read)

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
                inst_dec.enable_signal('HLT')
            elif c == ord('a') or c == ord('A'):
                clock.change_speed(-1)
            elif c == ord('z') or c == ord('Z'):
                clock.change_speed(1)
            elif c == ord('o') or c == ord('O'):
                clock.manual_pulse()
            elif c == curses.KEY_UP:
                mem.scroll_up()
            elif c == curses.KEY_DOWN:
                mem.scroll_down()
            elif c == ord('r') or c == ord('R'):
                inst_dec.reset()
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
