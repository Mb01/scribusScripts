#!/usr/bin/env python

# Here's a script to scramble words on each line in a text file
# usage ./scrambleSentences.py ~/path/to/filename

import os
import random
import sys

# TODO make this for scribus script

data = open(sys.argv[1]).read().split('\n')

#data is now a list of sentence strings

data = [x.split(' ') for x in data]

[random.shuffle(x) for x in data]

data = [' '.join(x) for x in data]

data = '\n'.join(data)

out = open('scrambled.txt',"w")

out.write(data)

out.close()

