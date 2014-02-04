import string
import random
import os

# I wrote this where I had to move between computers and OSs several times a day
USING_USB = True #are we running python from the usb drive
USING_WINDOWS = True
DIRECTORY = "programs" #or whatever
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def moveToBaseDir():
    drivePrefix = os.path.splitdrive(os.getcwdu())[0]
    os.chdir(drivePrefix+ '\\')

if USING_UBS and USING_WINDOWS:
    moveToBaseDir()

os.chdir(DIRECTORY)

infile = open(INPUT_FILE, "r")
test = infile.read()
infile.close()

#make the table
lower = string.ascii_lowercase
table = [x for x in lower]
random.shuffle(table)
table = "".join(table)

#encrypt
test = test.lower()

output = []

for x in test:
    if x in lower:
        output.append(table.find(x))
    else:
         output.append(x)

for x in range(len(output)):
    if type(output[x]) == type(1):
        output[x] = lower[output[x]]

output = "".join([str(x) for x in output])

#write the output to file

output += "\n" + lower + "\n" + table
out = open(OUTPUT_FILE,"w+")
out.write(output)
out.close()
