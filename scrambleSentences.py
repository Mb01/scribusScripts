
import os
import random

def moveToBaseDir():
    drivePrefix = os.path.splitdrive(os.getcwdu())[0]
    os.chdir(drivePrefix+ '\\')
#get the input
moveToBaseDir()
os.chdir("programs")

data = open('input.txt').read().split('\n')

#data is now a list of sentence strings

data = [x.split(' ') for x in data]

[random.shuffle(x) for x in data]

data = [' '.join(x) for x in data]

data = '\n'.join(data)

out = open('output.txt',"w+")

out.write(data)

out.close()

