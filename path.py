# Find the path
# 2 points

import sys


# This class will help us store the data
class GridNode(object):
  """
  Each one of these represents a square in the grid.
  """

  # Constructor for GridNode
  # Parameters: the data to be stored at the node
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.marked = False

  # Method to set the data
  def setData(self, data):
    self.data = data

  # Method to look at data
  def getData(self):
    return self.data

  # Method to set the node as marked
  def mark(self):
    self.marked = True

  # Method to look at marked or not
  def isMarked(self):
    return self.marked


# Opens the file
def openFile():
  # The input
  # Expected cmd input: python anagrams.py filename
  args = sys.argv[1:]
  # If there was no filename given
  if not args:
    print("Please specify a filename.")
    sys.exit(1)

  # At this point, we should have the file
  # Let's open it up
  filename = args[0]
  inputFile = open(filename, "r")
  return inputFile


# this function will create the grid for us
# Params: the file that has the dimensions
# Returns: an empty grid
def createGrid(inputFile):
    # These will hold the number of rows and numbers
  rows = 0
  columns = 0
  # Let's set the rows and numbers
  for line in inputFile:
    if rows == 0:
      columns = len(line)
    rows = rows + 1

  # Now let's make a 2D array to hold the grid
  grid = [[GridNode("") for j in range(columns)] for i in range(rows)]
  # print(str(grid))
  return grid


# This function will fill the grid for us
# Params: the grid and the file to read from
# Returns: nothing
def fillGrid(grid, inputFile):
  # Now let's go through and set all the elements in the grid
  # Reset the file back to the top, plus one line
  inputFile.seek(0)
  inputFile.readline()
  col = 0
  row = 0
  # Go through and fill in the grid
  for line in inputFile:
    # print(line)
    for char in line:
      grid[row][col].setData(char)
      col = col + 1
    col = 0
    row = row + 1


# This function checks if the node in the grid
# matches the data
# If it is correct, it will return True
def checkIfCorrect(grid, row, col, string, charPos):
  result = False
  if not grid[row][col].isMarked() and grid[row][col].getData() == \
     string[charPos]:
    grid[row][col].mark()
    result = True
  return result


# This function checks the four sides of a node
# Returns True if the entire grid is solved
def checkFourSides(grid, row, col, string, charPos):
    # Check if we're done
    if charPos == len(string):
      return True

    result = False
    # Check if the node to the top is correct
    if (not row == 0):
      found = checkIfCorrect(grid, row - 1, col, string, charPos)
      if found:
        result = checkFourSides(grid, row - 1, col, string, charPos + 1)
        if result:
          return True

    # Check if the node to the right is correct
    if (not col == len(grid[0]) - 1):
      found = checkIfCorrect(grid, row, col + 1, string, charPos)
      if found:
        result = checkFourSides(grid, row, col + 1, string, charPos + 1)
        if result:
          return True

    # Check if node to the bottom is correct
    if (not row == len(grid) - 1):
      found = checkIfCorrect(grid, row + 1, col, string, charPos)
      if found:
        result = checkFourSides(grid, row + 1, col, string, charPos + 1)
        if result:
          return True

    # Check if node to the left is correct
    if (not col == 0):
      found = checkIfCorrect(grid, row, col - 1, string, charPos)
      if found:
        result = checkFourSides(grid, row, col - 1, string, charPos + 1)
        if result:
          return True

    # At this point, looks like you've hit a dead end
    return False


# This function replaces all nonmarked nodes with periods
# And it prints out the entire matrix
def cleanUpGrid(grid, maxRow, maxCol):
  for i in range(maxRow):
    for j in range(maxCol):
      if not grid[i][j].isMarked():
        grid[i][j].setData(".")
      print(grid[i][j].getData(), end="")
    print("")


# The main body of the program
def main():
  inputFile = openFile()

  # This will hold the string we're looking for
  endString = inputFile.readline().strip()
  # Let's create the grid and fill it
  grid = createGrid(inputFile)
  fillGrid(grid, inputFile)

  # We know the top left corner is correct
  grid[0][0].mark()

  solved = False
  # Recursive function that goes through the entire grid
  # If it solves the grid, will return True
  solved = checkFourSides(grid, 0, 0, endString, 1)
  if not solved:
    print("Error: Could not find path")
    sys.exit(1)

  # At this point, the grid will be solved
  # Let's replace all unmarked Nodes with dots
  cleanUpGrid(grid, len(grid), len(grid[0]))

  # Done!
  pass


# If main
if __name__ == '__main__':
  main()
