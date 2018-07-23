#!/usr/bin/env python3
import curses
from curses import wrapper
import argparse
from pathlib import Path

import const
from interface import Interface


if __name__ == "__main__":

    curses_gui = Interface()
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('infile', help='name of the file to execute')
    args = parser.parse_args()
    input_file = Path(args.infile)
    if not input_file.is_file():
        print("Input file {} does not exist".format(args.infile))
        exit()

    wrapper(curses_gui.go, args.infile)
