#Calendar.py

from graphics import *

#Creating a window

def drawBox(myWin):
  """An example function of how to draw a box.
  Also important to see how to pass a window to another function."""

  topLeft = Point(20, 100)
  bottomRight = Point(50, 130)
  box = Rectangle(topLeft, bottomRight)
  box.draw(myWin)

def getClick(myWin):
  """This is an example function that will pause the program until the
  user clicks the mouse in the given window. Then the coordinates of
  the click is displayed in the window"""

  clickPoint = myWin.getMouse()
  coords = str(clickPoint.getX()) + ", " + str(clickPoint.getY())
  clickText = Text(clickPoint, coords)
  clickText.draw(myWin)


def main():
  win = GraphWin("Game", 640, 480)

  drawBox(win) #Draws a box
  getClick(win) #Click in the window then display coordinates of click.


if __name__ == '__main__':
  main()
