VAR sum 0x00

START:
# LOAD 0 into Reg B
LDBI 0x00
OUTB

# Load 1 int Reg A
LDAI 0x01

# Add the two registers
LOOP:
ADD

# Store Reg a into SUM
STA sum

# Copy the ALU into Reg A and load SUM into Reg B
LDAE
LDB sum

# Display Reg B
OUTB

# If the ALU overflowed jump to the beginning
JMPO START

# Jump back to the ADD to loop through again
JMP LOOP
