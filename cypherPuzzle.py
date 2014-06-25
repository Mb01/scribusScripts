import string
import random
import sys


infile = open(sys.argv[1], "r")
test = infile.read()
infile.close()

# this is the key
lower = string.ascii_lowercase
table = [x for x in lower]
random.shuffle(table)
table = "".join(table)

test = test.lower()

output = []

for x in test:
    if x in lower:
        
        output.append(table.find(x))
    else:
        # not a letter, keep spaces and periods etc...
         output.append(x)

# optionally replace the integers with letters
for x in range(len(output)):
    if type(output[x]) == int:
        output[x] = lower[output[x]]

# append the answer to the file
output = "\n" + " ".join([str(x) for x in output])
output += "\n" + lower + "\n" + table

out = open(OUTPUT_FILE,"w+")
out.write(output)
out.close()
