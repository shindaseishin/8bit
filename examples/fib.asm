# LOAD 0 into Reg B
LDBI 0x00 # this is an end of line comment
OUTB

LDAI 0x01
ADD
STA 0xFF

LDAE
LDB 0xFF

OUTB
JMPO 0x00
JMP 0x06
