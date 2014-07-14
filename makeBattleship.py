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

"""
This program makes essentially a table, originally intended for making educational worksheets where the target language represents the
co-ordinates of a square.
"""

# NOTE this program makes a table and lacks some of the functionality I've put into toolbox.py so it may be a scrap

# TODO, rename program file ... the file itself is/should be scrubbed of any reference 

import time
import os

# TODO: I made this program to be runnable on a usb drive on Windows, probably want to remove this
# but we still need a way to find the input text
# idea, we could change these to selected text-boxes

CURDIR = "F:"
os.chdir(CURDIR)
rows = open(os.path.join(CURDIR+'rows.txt') ,'r').read()
cols = open(os.path.join(CURDIR+'cols.txt'),'r').read()

ROWS = rows.split(' ')
COLS = cols.split(' ')

NUMROWS = len(ROWS) +1 #+1 for a row of lables
NUMCOLS = len(COLS) +1 #a column for lables

#MARGINS = (25,25,25,30)# (left, right, top, bottom) 
#newDocument(PAPER_A4, MARGINS, PORTRAIT, 1, UNIT_POINTS, UNIT_POINTS, 0, 1)
name = "output" + str(time.ctime())
name = name.replace(':', '')
FONT = 'Garamond Regular'
FONT_SIZE = 30


#createText(x, y, width, height) -> #string which is name
#this would be to wrap in an object
def custCreateTable(x, y, width, height, numrows, numcols):
	"""creates a table and returns the names of the text boxes"""
	pos = [x, y]
	colwidth = width / numcols
	rowheight = height / numrows
	names = []
	for row in range(numrows):
		pos[0] = x 
		for col in range(numcols):
			names.append(createText(pos[0], pos[1], colwidth, rowheight))
			pos[0] += colwidth
		pos[1] += rowheight
	return names

def makeTable():
	names = custCreateTable(60,226,473,422, NUMROWS, NUMCOLS)
	leftCol = [x for x in names if names.index(x) % NUMCOLS == 0][1:]
	topRow  = names[1:NUMCOLS]# so what we have are the left column and top row without their intersection
	for x in range(len(leftCol)):#to avoid a bug if there are two identical strings in row lables
		setText(ROWS[x], leftCol[x])
	for x in range(len(topRow)):
		setText(COLS[x], topRow[x])
	return names, leftCol, topRow

names, leftCol, topRow = makeTable()

#Set the font and such
for x in names:
	font_size = FONT_SIZE
	setFont(FONT, x)
	setFontSize(font_size, x)
	setTextAlignment(ALIGN_CENTERED, x)
	while textOverflows(x):
		font_size -= 1
		setFontSize(font_size, x)

saveDocAs(name)
