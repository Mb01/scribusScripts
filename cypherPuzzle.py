
import string
import random
import os


def moveToBaseDir():
    drivePrefix = os.path.splitdrive(os.getcwdu())[0]

    os.chdir(drivePrefix+ '\\')

#get the input

moveToBaseDir()
os.chdir("programs")

test = open("input.txt", "r").read()

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

#save

output += "\n" + lower + "\n" + table

out = open("output.txt","w+")

out.write(output)

out.close()







