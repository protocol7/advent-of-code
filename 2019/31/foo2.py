import sys
from intcode import *
from intasm import *


# ChronalCode day 19 part 1 in Intcode  (https://adventofcode.com/2018/day/19)

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

     # read input
     inp ipr
     mul ipr -1 nipr

     rb 200000
     add 0 0 len
inlo:inp o
     # check if we're done
     eq o -1 tmp
     jit tmp indone

     add o 0 &0
     rb 1
     inp a
     add a 0 &0
     rb 1
     inp b
     add b 0 &0
     rb 1
     inp c
     add c 0 &0
     rb 1

     add len 1 len
     jit 1 inlo

indone:mul len -4 tmp
     rb tmp
     rb -200000

     rb ipr
     add -1 0 &0
     rb nipr

loop:rb ipr
     add &0 1 &0
     add &0 0 ip
     rb nipr

     # check that ip is within the program
     lt ip len tmp
     jif tmp outp
     lt ip 0 tmp
     jit tmp outp


     mul ip 4 adr
     add 200000 adr adr
     rb adr
     add &0 0 o
     rb 1
     add &0 0 a
     rb 1
     add &0 0 b
     rb 1
     add &0 0 c
     add adr 3 adr
     mul adr -1 adr
     rb adr

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

opcodes = {"gtri": 0,
            "bani": 1,
            "eqrr": 2,
            "gtir": 3,
            "eqir": 4,
            "bori": 5,
            "seti": 6,
            "setr": 7,
            "addr": 8,
            "borr": 9,
            "muli": 10,
            "banr": 11,
            "addi": 12,
            "eqri": 13,
            "mulr": 14,
            "gtrr": 15}

def parse(line):
    t = line.strip().split(" ")
    if line[0] == "#":
        return [int(t[1])]
    else:
        t[0] = opcodes[t[0]]
        return map(int, t)

inp = flatmap(parse, sys.stdin)
inp += [-1]
print(inp)
inp = iter(inp)


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
