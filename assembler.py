#!/usr/bin/env python3

import argparse
from pathlib import Path

def str2bool(v):
    """Convert various string values to a boolean
    For example 'yes' == true and 'no' == false
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# parse command line arguments
parser = argparse.ArgumentParser(description='Compile asm file to byte code')
parser.add_argument('-i', '--infile', dest='infile', help='name of the file to compile')
parser.add_argument('-o', '--outfile', dest='outfile', help='filename for the compiled output')
parser.add_argument('-w', '--overwrite', type=str2bool, nargs='?', const=True, help='Overwrite output file if it already exists')
args = parser.parse_args()

errors = [];
if args.infile == None:
    errors.append("Input filename is required")
else:
    input_file = Path(args.infile)
    if not input_file.is_file():
        errors.append("Input file {} does not exist".format(args.infile))

if args.outfile == None:
    errors.append("Output filename is required")
else:
    output_file = Path(args.outfile)
    if output_file.is_file() and not args.overwrite:
        errors.append("Output file {} exists. Aborting. Use the --overwrite option to replace the file".format(args.outfile))

if len(errors) > 0:
    print(*errors, sep='\n')
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

variables = {}
labels = {}

with open(args.outfile, 'wb') as outfile, open(args.infile, 'r') as infile:
    compiled = bytearray([0x00]*256)
    pointer = 0
    for line in infile:
        # tokenize the current line
        line = line.split()
        # Make everything uppercase
        [x.upper() for x in line]

        # Skip empty lines and full line comments
        if len(line) == 0 or line[0][0] == '#':
            continue

        # Process variable declarations
        if line[0] == 'VAR':
            if line[1] in variables:
                raise Exception("Variable {} declared more than once".format(line[1]))
            # Reserve memory space for the variable
            variables[line[1]] = 255 - len(variables)
            # set the initial value for the variable
            # TODO: make the value optional
            compiled[variables[line[1]]] = int(line[2],16)

        # Process label declarations
        elif line[0][-1] == ':':
            labels[line[0][:-1]] = pointer
        # If all other tests failed then the only option left is an instruction
        else:
            # Add the opcode for the current instruction at the current position
            compiled[pointer] = tokens[line[0]]
            # Set the second byte to 0 if the opcode has no argument or there is a comment
            if len(line) == 1 or line[1][0] == '#':
                compiled[pointer+1] = 0x00
            # If the argument is a variable reference, put the variable address into the argument
            elif line[1] in variables:
                compiled[pointer+1] = variables[line[1]]
            # If the instruction is a jump add the label address to the ArgumentTypeError
            # TODO: Add error checking to make sure that the label exists before using it.
            elif line[1] in labels and line[0][0:3] == 'JMP':
                compiled[pointer+1] = labels[line[1]]
            # Else just use the argument as is
            else:
                compiled[pointer+1] = int(line[1],16)

            # Move the memory pointer forward to the next 2 byte boundry
            pointer += 2
            # Make sure the program isn't too big to fit in memory
            if pointer > (256 / 2) - len(variables):
                exit("Program too large to fit memory")

    outfile.write(compiled)
