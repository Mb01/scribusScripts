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
a program for ruling pages and some utilities for costumizing
"""

from scribus import *

width, height = getPageSize()
top_margin, left_margin, right_margin, bottom_margin = getPageMargins()

# *this I believe is the way to go with margin getting*
# change to absolute positions
# we now have the x position of the right_margin
# and the y position of bottom margin
right_margin = width - right_margin
bottom_margin = height - bottom_margin


# TODO, take a type (dotted, solid) to draw
def drawLine(y, x=left_margin):
    """ here we'll just draw a line from the specified x to the end of the page"""
    name = createLine(x, y, right_margin, y)
    return name

def draw4Rules(spacing, y, x=left_margin):
  """pass this function to rulePage for penmanship paper"""
  for i in range(4):
    name = drawLine(y)
    if i == 1:
      setLineStyle(LINE_DASH, name)
    if i != 2:
      setLineWidth(0.5,name)
    y += spacing
  return y

def drawRule(spacing, y):
  """Pass this function to rulePage for "normal" rules"""
  drawLine(y)
  return y + spacing


def rulePage(spacing, function):
  """ rulePage takes a function which draws a rule with spacing of "spacing" at position y and returns
a new position y to continue ruling from. """
  y = top_margin
  while y < bottom_margin:
    y = function(spacing, y)
    y += spacing

def get_coordinates_from_user():
    return [int(p) for p in valueDialog("enter location", "type the location of the upper ledt corner as \"x,y\"").split(',')]

def user_dialog_draw_4(spacing=10):
  """allow the user to determine where the thing goes"""
  x,y = get_coordinates_from_user()
  for _ in range(4):
    name = drawLine(y,x)
    if x == 1:
      setLineStyle(LINE_DASH, name)
    if x != 2:
      setLineWidth(0.5,name)
    y += spacing
  return y

def rule10():
  rulePage(10, draw4Rules)

user_dialog_draw_4()
