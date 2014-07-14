"""Only runs with scribus scripter unless define api functions, perhaps by some scribus module"""
"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

For a copy of the GNU General Public License see http://www.gnu.org/licenses/

Copyright Mark Bowden 2013, 2014
"""

# NOTE: without really reading through this I think it may be the most useful file in this collection
# it wraps and enhances a number of the API's with some sensible names

# get everything into variables
margins = getPageMargins()# (Top Left Right Bottom)
pageSize = getPageSize()

# this gets names of the created text boxes, there's a user interface for this but this
# is a quick and dirty way for our script to get the names in a nice Python list in the correct order
def createTable(originX, originY, width, height, numCols, numRows):
  names = []
  #print each column out
  for curRow in range(numRows):
    for curCol in range(numCols):
      x = originX + curRow * height
      y = originY + curCol * width
      names.append(createText(x, y, width, height))
  return names

# given the names from the result of createTable, rotate the top row by degrees degrees
def rotateTopRow(names, numberOfCols, degrees):
  """Rotates the first numberOfCols elements in names by degrees to create rotated labels for tables"""
  """This is made to work with tables created with createTable"""
  topRow = names[::numberOfCols]
  for x in topRow:
    rotateObject(degrees,x)
#example of how to use
#names = createTable(40,40,80,80,5,6)
#rotateTopRow(names, 5, 35)

def getSelectedObjects():
  """ get a list of all selected objects"""
  objects = []
  for x in range(selectionCount()):
    objects.append(getSelectedObject(x))
  return objects

# a useless function
def setFontSmallArial():
  #setTextDistances(left, right, top, bottom, ["name"])
  for x in objects:
     #setTextDistances(0,0,20,0,x)
     setFont("Arial Regular",x)
     setFontSize(10, x)

# a useful function I believe
def scrambleSentences(data):
    data = data.split('\n')
    data = [x.split(' ') for x in data]
    [random.shuffle(x) for x in data]
    data = [' '.join(x) for x in data]
    data = '\n'.join(data)
    return data

# a useful function I believe
def scrambleWords(data):
    '''Somehow removing all newlines... probably related to \r'''
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

def scramble_words_selected():
    """scrambles the words in a selected text box"""
    setText(scrambleWords(getText()))
