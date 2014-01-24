import os
import random

def moveToBaseDir():
    drivePrefix = os.path.splitdrive(os.getcwdu())[0]
    os.chdir(drivePrefix+ '\\')

#get the input
moveToBaseDir()
os.chdir("programs")

data = open('input.txt').read().lower().split('\n')
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

out = open('output.txt',"w")
out.write(output)
out.close()

