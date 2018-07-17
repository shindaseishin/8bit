#!/usr/bin/env python3

import argparse
from pathlib import Path


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-i', '--infile', dest='infile', help='name of the file to compile')
parser.add_argument('-o', '--outfile', dest='outfile', help='filename for the compiled output')
parser.add_argument('-w', '--overwrite', type=str2bool, nargs='?', const=True, help='Overwrite output file if it already exists')

args = parser.parse_args()

if args.infile == None:
    print("Input filename is required")
    exit()
else:
    input_file = Path(args.infile)
    if not input_file.is_file():
        print("Input file {} does not exist".format(args.infile))
        exit()

if args.outfile == None:
    print("Output filename is required")
    exit()
else:
    output_file = Path(args.outfile)
    if output_file.is_file() and not args.overwrite:
        print("Output file {} exists. Aborting. Use the --overwrite option to replace the file".format(args.outfile))
        exit()


tokens = {
    "NOOP" : 0x00,
    "LDA"  : 0x01,
    "STA"  : 0x02,
    "LDAI" : 0x03,
    "LDAE" : 0x04,
    "LDB"  : 0x05,
    "STB"  : 0x06,
    "LDBI" : 0x07,
    "LDBE" : 0x08,
    "STE"  : 0x09,
    "ADD"  : 0x0A,
    "SUB"  : 0x0B,
    "JMP"  : 0x0C,
    "JMPC" : 0x0D,
    "JMPO" : 0x0E,
    "OUT"  : 0x1B,
    "OUTI" : 0x1C,
    "OUTA" : 0x1D,
    "OUTB" : 0x1E,
    "HLT"  : 0x1F
}

with open(args.outfile, 'wb') as outfile, open(args.infile, 'r') as infile:
    for line in infile:
        compiled = bytearray([0x00, 0x00])

        inst, *operand = line.split()
        if inst[0] != '#':
            if not operand or operand[0] == '#':
                operand = 0x00
            else:
                operand = int(operand[0],16)

            compiled[0] = tokens[inst.upper()]
            compiled[1] = operand
            outfile.write(compiled)
