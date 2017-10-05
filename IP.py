# Validating IP addresses
# 1 point

import sys
import re


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


# Main code
def main():
  inputFile = openFile()

  # +++++ Begin code +++++
  # We'll use these to hold ip addresses
  IPbegin = ""
  IPend = ""
  IPcur = ""
  # And we'll use this to hold the line
  curLine = ""

  # Look at each line of the input file
  for line in inputFile:
    # Split the entire line into IP addresses
    pattern = r"""
      (\d+?\.\d+?\.\d+?\.\d+?)\   # IP Address 1
      (\d+?\.\d+?\.\d+?\.\d+?)\   # IP Address 2
      (\d+?\.\d+?\.\d+?\.\d+?)    # IP Address 3
      """
    curLine = re.search(pattern, line, re.VERBOSE)

    # If it could not be found (i.e. syntax was incorrect)
    if not curLine:
      print("InValid")
    # If it could be found
    else:
      IPbegin = curLine.group(1)
      IPend = curLine.group(2)
      IPcur = curLine.group(3)
      # print(IPbegin + " " + IPend + " " + IPcur)

    # We have all our IP addresses.
    # Let's check if the last one is in range


  # Done with the program
  pass


if __name__ == '__main__':
  main()
