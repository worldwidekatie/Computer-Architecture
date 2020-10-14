"""Number Bases"""
# Base 2 - binary
# Base 8 - octal
# Base 10 - decimal
# Base 16 - hexadecimal ("hex")
# Base 64 - 'base 64'

"""Base 10"""
# Digits 0-9

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Now we've run out of digits! So we need another digit
# to represent how many things we have. So 10 means we have
# one ten and zero ones. 11 means one ten and one one.
# 12 means I have one ten and two ones (1*10 + 2*1).

# ...
# 98
# 99
# 100 (one one-hundred, zero tens, and zero ones)

# 1s = 10^0
# 10s = 10^1
# 100s = 10^2
# 1000s = 10^3

"""Binary"""
# 0's and 1's
# Binary Digits: 0-1 (aka "bits")

# 0
# 1
# 10 (2)
# 11 (3)
# 100 (4)
# 101 (5)
# 110 (6) one 4, one 2, zero 1s = 1*4 + 1*2 + 0*1 = 6
# 111 (7)
# 1000 (8)

# ||||
# ||| +-------- 1s
# || +--------- 2s
# | +---------- 4s
# +------------ 8s

# 1s = 2^0
# 2s = 2^1
# 4s = 2^2
# 8s = 2^3
# 16s = 2^4

# binary 110 is decimal 6
# The number base is important when you
# write the number down so you have to specify the base.

# E.g. if you tell someone you're going to give them
# $110000 it's important to know if it's in binary.
# Because if so it's $48. 

# To swith python to binary, you have to tell it to do binary

# Prefix the number with an indicator of the base.
# 0b for binary
# 0x for hex
# 0o for octal (very rarely used.)

# 0b110 -> 6
print(0b110) # prints 6

print(0xC) # prints 12 from hex
print(0b1100) # prints 12 from binary 

print(bin(12)) # prints 0b110

a = 12
print(f'{a:x}') # prints 'c', converts to hex
print(f'{a:b}') # prints 1100, converts to binary


"""Hex"""

# Digits 0-9, A-F because we need 16 digits
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# a
# b
# c
# d
# e
# f
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 1a
# 1b
# 1c
# 1d
# 1e
# 1f
# 20

# RR GG BB
# ff 02 1d

0x87 # == 0b??????????
# 1 hex digit == 4 binary digit
# So to convert, split each hex digit,
# convert it to binary, then put it
# back together again.

# 0x    8      7
# 0b   ????   ????
# 0b   1000   0111
# 0b10000111 == 0x87
print(0x87)
print(0b10000111)

#        0x0C
# 0x    0    C (12 decimal)
# 0b  0000  1100 (one eight, plus one four, plus zero two and zero ones)
# 0b   00001100

# 0xFF
# 0x    F     F (F is 15 decimal)
# 0b  1111   1111 (one 8, one 4, one 2, one 1)
# 0b    11111111

# 8 bits == '1 byte'
# 4 bits == '1 nybble'

# 00001101 use leading zeroes to show you're talking about a byte
# b/c memory in the computer is stored 8 bits at a time

# 255 is the largest value you can store in a byte/slot
# which is also 
# 0b11111111 or 0xff

# 1 one
# 1 two
# 1 four
# 1 eight
# 1 sixteen
# 1 thirty two
# 1 sixty four
# 1 hundred twenty eight

# 128 + 64 + 32 + 16 + 8 + 4 + 1 = 255

# F ones
# F sixteens


"""Emulator Program"""
# A program that runs programs
# Be able to print out Beej and halt, that's it.
import sys
# Memory 
# -------------------
# holds bytes
#
# Big array of bytes
# To get or set data in memory, you need the index
# in the array
#
# These terms are equivalent:
## *Index into the memory array
## *Address
## *Location
## *Pointer
memory = [
    1, # PRINT_BEEJ
    1, # PRINT_BEEJ
    1, # PRINT_BEEJ
    2, # HALT
    1 # PRINT_BEEJ
]
"""Simplest Implementation """
# for instruction in memory:
#     if instruction == 1:
#         print("Beej!")

#     elif instruction == 2:
#         break

"""Implementation with a Counter"""
# Keep track of the address of the currently-executing instruction
# pc = 0 # program counter, pointer to the instruction we're exectuing
# halted = False

# while not halted:
#     instruction = memory[pc]

#     if instruction == 1:
#         print("Beej!")
#         pc += 1

#     elif instruction == 2:
#         halted = True
#         pc += 1

"""Implementation with a Variables"""
# Variables are called "registers"
## * There are a fixed number of them
## * They have fixed names: R0, R1, R2 ... R7
## * Registers can each hold a single byte of data
# "opcode" == the instruction byte
# "operands" == arguments to the instruction

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3

memory = [
    1, # PRINT_BEEJ
    3, # SAVE_REG-> save 37 in R1 (r1 = 37)
    1, # Which R we're storing in
    37, # number we're storing
    4, # PRINT_REG->             (print(r[1]))
    1, # R1
    1, # PRINT_BEEJ
    1, # PRINT_BEEJ
    2 # HALT
]

register = [0] * 8 #[0, 0, 0, 0, 0, 0, 0]

pc = 0 
halted = False

while not halted:
    instruction = memory[pc]

    if instruction == 1: # PRINT_BEEJ
        print("Beej!")
        pc += 1

    elif instruction == 2: # HALT
        halted = True
        pc += 1
    
    elif instruction == 3: # SAVE_REG
        reg_num = memory[pc+1]
        value = memory[pc+2]
        register[reg_num] = value
        print(register)
        pc += 3

    elif instruction == 4: # PRINT_REG
        reg_num = memory[pc+1]
        print(register[reg_num])
        pc += 2
    
    # else:
    #     print(f"unknown instruction {instruction}")
    #     sys.exit(1)


"""Day 2 Notes"""
import sys

# Memory
# ------
# Holds bytes
#
# Big array of bytes
#
# To get or set data in memory, you need the index in the array
#
# These terms are equivalent:
# * Index into the memory array
# * Address
# * Location
# * Pointer

# "opcode" == the instruction byte
# "operands" == arguments to the instruction

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4

memory = [
	1,   # PRINT_BEEJ
    3,   # SAVE_REG R1,37    r[1] = 37
	1,   # R1
	37,
	4,   # PRINT_REG R1      print(r[1])
	1,   # R1
	1,   # PRINT_BEEJ
	2    # HALT
]

# Variables are called "registers".
# * There are a fixed number
# * They have preset names: R0, R1, R2, R3 ... R7
#
# Registers can each hold a single byte

register = [0] * 8  # [0,0,0,0,0,0,0,0]


# Start execution at address 0

# Keep track of the address of the currently-executing instruction
pc = 0   # Program Counter, pointer to the instruction we're executing

halted = False

while not halted:
	instruction = memory[pc]

	if instruction == PRINT_BEEJ:
		print("Beej!")
		pc += 1

	elif instruction == HALT:
		halted = True
		pc += 1

	elif instruction == SAVE_REG:
		reg_num = memory[pc + 1]
		value = memory[pc + 2]
		register[reg_num] = value
		pc += 3

	elif instruction == PRINT_REG:
		reg_num = memory[pc + 1]
		print(register[reg_num])
		pc += 2

	else:
		print(f"unknown instruction {instruction} at address {pc}")
		sys.exit(1)