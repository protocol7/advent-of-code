import sys
from intcode import *
from intasm import *


# Day 31: implement a ChronalCode (https://adventofcode.com/2018/day/16) VM in
# Intcode and run the input program to solve 2018/16 part 2. If you haven't
# solved part 1, and the first half of part 2 (resolving opcodes) already, it
# can be solved in any language of your choice (it's the AoC author's favorite
# problem, so worth solving). The input program is provided to your Intcode as
# a sequence of integers, not ASCII. Terminate the sequence with -1.
#
# Thus, the sample ChronalCode program:
# 6 3 2 1
# 12 1 4 2
# 8 1 2 0
#
# is input into the intcode as:
# 6, 3, 2, 1, 12, 1, 4, 2, 8, 1, 2, 0, -1
#
# Assuming the opcodes: 6=seti, 12=addi, 8=addr, the output (the value in register 0) would be 10.

asm = """
     # pre-generate pow2 table
     add 1 0 b
     rb 200064

btbl:add b 0 &0
     rb -1
     mul b 2 b
     eq b 18446744073709551616 tmp # 2^64
     jif tmp btbl

     rb -100000
     # done generating pow2 table

loop:inp o

     # check if we're done
     eq o -1 tmp
     jit tmp outp

     inp a
     inp b
     inp c
     mul a -1 na
     mul b -1 nb
     mul c -1 nc

     eq o 0 tmp
     jit tmp gtri

     eq o 1 tmp
     jit tmp bani

     eq o 2 tmp
     jit tmp eqrr

     eq o 3 tmp
     jit tmp gtir

     eq o 4 tmp
     jit tmp eqir

     eq o 5 tmp
     jit tmp bori

     eq o 6 tmp
     jit tmp seti

     eq o 7 tmp
     jit tmp setr

     eq o 8 tmp
     jit tmp addr

     eq o 9 tmp
     jit tmp borr

     eq o 10 tmp
     jit tmp muli

     eq o 11 tmp
     jit tmp banr

     eq o 12 tmp
     jit tmp addi

     eq o 13 tmp
     jit tmp eqri

     eq o 14 tmp
     jit tmp mulr

     eq o 15 tmp
     jit tmp gtrr

     jit 1 unkn

seti:rb c
     add a 0 &0
     rb nc
     jit 1 loop

setr:rb a
     add &0 0 tmp
     rb na
     rb c
     add tmp 0 &0
     rb nc
     jit 1 loop

muli:add b 0 bb
     jit 1 mul

mulr:rb b
     add &0 0 bb
     rb nb
     jit 1 mul

mul: rb a
     add &0 0 tmp
     rb na
     rb c
     mul tmp bb &0
     rb nc
     jit 1 loop

addi:add b 0 bb
     jit 1 add

addr:rb b
     add &0 0 bb
     rb nb
     jit 1 add

add: rb a
     add &0 0 tmp
     rb na
     rb c
     add tmp bb &0
     rb nc
     jit 1 loop

eqri:rb a
     add &0 0 aa
     rb na
     add b 0 bb
     jit 1 eq

eqir:add a 0 aa
     rb b
     add &0 0 bb
     rb nb
     jit 1 eq

eqrr:rb a
     add &0 0 aa
     rb na
     rb b
     add &0 0 bb
     rb nb
     jit 1 eq

eq  :rb c
     eq aa bb tmp
     add tmp 0 &0
     rb nc
     jit 1 loop

bani:add 2 0 bop
     add 1 0 bimm
     jit 1 bb

banr:add 2 0 bop
     add 0 0 bimm
     jit 1 bb

bori:add 1 0 bop
     add 1 0 bimm
     jit 1 bb

borr:add 1 0 bop
     add 0 0 bimm
     jit 1 bb

bb:  rb a
     add &0 0 tmp
     rb na
     add tmp 0 aa

     jit bimm bbb

     # read b register
     rb b
     add &0 0 tmp
     rb nb
     add tmp 0 bb
     jit 1 bb0

     # use by immediate
bbb: add b 0 bb

bb0: add 0 0 cc

     # move into pow2 table
     rb 100000

     # check bit for aa
bb1: add 0 0 cx
     add &0 0 bit
     mul bit -1 nbit
     lt aa bit tmp
     jit tmp bb2
     add aa nbit aa
     add 1 0 cx

     # check bit for bb
bb2: lt bb bit tmp
     jit tmp bb3
     add bb nbit bb
     add cx 1 cx

bb3: lt cx bop tmp
     jit tmp bb4
     add cc bit cc

bb4: rb 1
     eq bit 1 tmp
     jif tmp bb1

     # done with the pow2 table
     rb -65
     rb -100000

     rb c
     add cc 0 &0
     rb nc
     jit 1 loop

gtri:rb a
     add &0 0 aa
     rb na
     add b 0 bb
     jit 1 gt

gtir: add a 0 aa
     rb b
     add &0 0 bb
     rb nb
     jit 1 gt

gtrr:rb a
     add &0 0 aa
     rb na
     rb b
     add &0 0 bb
     rb nb
     jit 1 gt

gt:  rb c
     lt bb aa tmp
     add tmp 0 &0
     rb nc
     jit 1 loop

unkn:out -999
     jit 1 done

outp:out &0

done:ext
"""

def parse(line):
    return map(int, line.strip().split(" "))

inp = iter(flatmap(parse, sys.stdin))

prog = intasm(asm)
print(",".join([str(x) for x in prog]))
print(len(prog))
print("")

ic = Intcode(prog, lambda: next(inp))

while True:
    o = ic.run()

    if o is None:
        break

    print(o)



