# Palindrome phrases
# 1 point

import sys


# Given a position in a line, it checks if it's a palindrome.
# It keeps going until it can't go anymore, and returns the palindrome string
def checkPalindrome(pos, line):
  # countPos is the forward count of the program
  # countNeg is the negative count of the program
  # result is the palindrome
  countPos = 1
  countNeg = 1
  result = ""
  # These two variables will be used to look at the line
  nextPos = ""
  nextNeg = ""

  # keep repeating until no more palindrome is found
  # or until you've looked at the entire line
  while (pos - countNeg >= 0) and (pos + countPos < len(line)):
    # We are looking at the previous and next chars that we haven't seen yet
    # If they are not alphanumeric, we skip it
    nextNeg = line[pos - countNeg]
    if not nextNeg.isalnum():
      countNeg = countNeg + 1
      continue
    nextPos = line[pos + countPos]
    if not nextPos.isalnum():
      countPos = countPos + 1
      continue

    # We have confirmed the positions of the previous and next characters
    # Compare to see if they are equal
    if nextNeg.lower() == nextPos.lower():
      result = line[pos - countNeg:pos + countPos + 1]
      countNeg = countNeg + 1
      countPos = countPos + 1
    else:
      break

  # If this is not the longest palindrome, then return nothing
  return result


# main program body
def main():
  # The input
  # Expected cmd input: python palindrome.py filename
  args = sys.argv[1:]
  # If there was no filename given
  if not args:
    print("Please specify a filename.")
    sys.exit(1)

  # At this point, we should have the file
  # Let's open it up
  filename = args[0]
  inputFile = open(filename, "r")

  # +++++ Begin code +++++
  # Do this for each input
  for line in inputFile:
    # To make sure we don't have any super short lines
    if len(line) <= 1:
      print(line)
      continue

    # pos is the character we are looking at
    # length is the length of the current palindrome
    # longest is the length of the longest palindrome
    # longestStr is the longest palindrome
    pos = 1
    length = 1
    longest = 1
    tmpStr = ""
    longestStr = ""

    # Logic: Look at each character and
    # check if it's the middle of a palindrome
    # skip the first character, as it can never be the center of a palindrome
    for char in line[1:]:
      tmpStr = checkPalindrome(pos, line)
      length = len(tmpStr)
      if length > longest:
        longest = length
        longestStr = tmpStr
      pos = pos + 1

    # By this point we've found the longest palindrome.
    # Print it out
    print(longestStr)

  # Done with the program
  pass


if __name__ == '__main__':
  main()
