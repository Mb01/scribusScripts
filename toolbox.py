"""Only runs with scribus scripter unless define api functions, perhaps by some scribus module"""

margins = getPageMargins()# (Top Left Right Bottom)
pageSize = getPageSize()

def createTable(originX, originY, width, height, numCols, numRows):
  names = []
  #print each column out
  for curRow in range(numRows):
    for curCol in range(numCols):
      x = originX + curRow * height
      y = originY + curCol * width
      names.append(createText(x, y, width, height))
  return names

def rotateTopRow(names, numberOfCols, degrees):
  """Rotates the first numberOfCols elements in names by degrees"""
  topRow = names[::numberOfCols]
  for x in topRow:
    rotateObject(degrees,x)
#example of how to use
#names = createTable(40,40,80,80,5,6)
#rotateTopRow(names, 5, 35)

def getSelectedObjects():
  objects = []
  for x in range(selectionCount()):
    objects.append(getSelectedObject(x))
  return objects

def setFontSmallArial():
  #setTextDistances(left, right, top, bottom, ["name"])
  for x in objects:
     #setTextDistances(0,0,20,0,x)
     setFont("Arial Regular",x)
     setFontSize(10, x)

def scrambleSentences(data):
    data = data.split('\n')
    data = [x.split(' ') for x in data]
    [random.shuffle(x) for x in data]
    data = [' '.join(x) for x in data]
    data = '\n'.join(data)
    return data

def scrambleWords(data):
    '''Somehow removeing all newlines... prolly related to \r'''
    data = data.lower().split()
    output = []
    for word in data:
        temp = [letter for letter in word]
        random.shuffle(temp)
        output.append(temp)
    #data is now list of lists
    output = [''.join(word) for word in output]
    #OUTPUT is now list of scrambled words
    #move punctuation and newlines to back of word
    #we need a regular expression with matching for this...
    output = [word.replace('.','') + '.' if '.' in word else word for word in output]
    output = [word.replace('?','') + '?' if '?' in word else word for word in output]
    output = [word.replace('!','') + '!' if '!' in word else word for word in output]
    output = [word.replace('\n','') + '\n' if '\n' in word else word for word in output]
    output = ' '.join(output)
    output = output.replace("\n ", "\n")
    return output

setText(scrambleWords(getText()))
