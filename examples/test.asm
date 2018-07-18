# Load 0 into register A
LDAI 0x00
# load 1 into register B
LDBI 0x01
# Display the contents of Register A
OUTA # No operand on OUT instruction
# Add A and B together
ADD
# store result in A
LDAE
#Load 43 into register B
LDBI 0x2B
# If registers A and B are equal jump to instruction 0x10
JMPC 0x10
# Jump to instruction 0x02
JMP 0x02
# Jump back to beginning to start counting again
JMP 0x00
# Halt the computer, should never reach here
HLT
