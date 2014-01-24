
#make a battleship game
import time
import os

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
name = "Battleship " + str(time.ctime())

name = name.replace(':', '')

FONT = 'Garamond Regular'
FONT_SIZE = 30
#createText(x, y, width, height) -> #string which is name
#this would be  to wrap in an object
def custCreateTable(x, y, width, height, numrows, numcols):
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

def testCreateCustomTable():
	custCreateTable(20, 20, 500, 200, 10,5 )

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

print names

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
