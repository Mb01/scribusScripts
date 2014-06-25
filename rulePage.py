# as of now the usage of this is copy and paste into scripter console

width, height = getPageSize()
top_margin, left_margin, right_margin, bottom_margin = getPageMargins()
#change to absolute positions
right_margin = width - right_margin
bottom_margin = height - bottom_margin

def drawLine(y):
  name = createLine(left_margin, y, right_margin, y)
  return name

def draw4Rules(spacing, y):
  """pass this function to rulePage for penmanship paper"""
  for x in range(4):
    name = drawLine(y)
    if x == 1:
      setLineStyle(LINE_DASH, name)
    if x != 2:
      setLineWidth(0.5,name)
    y += spacing
  return y

def drawRule(spacing, y):
  """Pass this function to rulePage for "normal" rules"""
  drawLine(y)
  return y + spacing

def rulePage(spacing, function):
  y = top_margin
  while y < bottom_margin:
    y = function(spacing, y)
    y += spacing

def rule10():
  rulePage(10, draw4Rules)

rule10()
