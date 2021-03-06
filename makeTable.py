from scribus import *


data = open('F:\\programs\\table.txt').read().split('\n')

for x in range(len(data)):
	data[x] = data[x].split(' ')

def createTable(x, y, width, height, data):
	pos = [x, y]
	numrows = len(data)
	numcols = max([len(dat) for dat in data])
	colwidth  = width / numcols
	rowheight = height / numrows
	names = []
	for row in range(numrows):
		names.append([])
		pos[0] = x
		for col in range(numcols):
			names[-1].append(createText(pos[0], pos[1], colwidth, rowheight))
			pos[0] += colwidth
		pos[1]  += rowheight
	return names

names =createTable(20,20,200,500, data)
flatData = [x for row in data for x in row]
flatNames = [x for row in names for x in row]

[setText(x,y) for x, y in flatData, FlatNames]
