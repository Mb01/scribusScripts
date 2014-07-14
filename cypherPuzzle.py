#!/usr/bin/env python
"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

For a copy of the GNU General Public License see http://www.gnu.org/licenses/

Copyright Mark Bowden 2013, 2014
"""

"""
This program, intended for making puzzles, provides ZERO cryptographic protection, as the puzzles are meant to be solved by
humans for recreational purposes. The output is triviably breakable by hand.
"""


# USAGE ./cypherPuzzle.py infile.txt outfile.txt

# TODO, integrate this into some module that generates worksheets in a modular fashion

import string
import random
import sys

# the program takes as input lines of text to turn into cipher puzzles
infile = open(sys.argv[1], "r")
test = infile.read()
infile.close()

test = test.lower()

# create a random lookup table which is the key, or solution to the puzzle
lower = string.ascii_lowercase
table = [x for x in lower]
random.shuffle(table)
random.shuffle(table)
random.shuffle(table)

table = "".join(table)
# table is now the key


output = []

# substitue each letter in the plaintext, "test," with it's position in the random "table"
# if it's not in the table, it's not a letter and we probably want commas and periods if they are in the plaintext.
for x in test:
    if x in lower:
        output.append(table.find(x))
    else:
        # not a letter, keep spaces and periods etc...
         output.append(x)
# output is now a mapping of the plaintext to the integer positions in the random "table": 0 .. 25
# we now convert those positions to their corresponding letter in the alphabet: a .. z
for x in range(len(output)):
    if type(output[x]) == int:
        output[x] = lower[output[x]]

# append the answer to the file
output = "\n" + " ".join([str(x) for x in output])
output += "\n" + lower + "\n" + table

outfile = open(sys.argv[2],"w+")
outfile.write(output)
outfile.close()
