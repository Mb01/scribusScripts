from scribus import *
from toolbox import *

name = valueDialog("Enter Name", "Name of object to get font from?")
font = getFont(name)
size = getFontSize(name)

for frame in gso():
	setFont(font, frame)
	setFontSize(size, frame)
	
