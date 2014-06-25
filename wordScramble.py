import os
import random
import sys

# usage ./wordScramble.py /path/to/infile.txt /path/to/outfile.txt

data = open(sys.argv[1]).read().lower().split('\n')
#data list of sentences

output = []
for sentence in data:
    for word in sentence.split(' '):
        if not word.isalpha():
            output.append(word)
            continue
        temp = [letter for letter in word]
        random.shuffle(temp)
        temp = ''.join(temp)
        output.append(temp)
    output.append('\n')


#OUTPUT is now list of scrambled words
#move newlines to back of word
output = [word.replace('.','') + '.' if '.' in word else word for word in output]
output = [word.replace('\n','') + '\n' if '\n' in word else word for word in output]
output = ' '.join(output)

output = output.replace("\n ", "\n")

out = open(sys.argv[2],"w")
out.write(output)
out.close()

