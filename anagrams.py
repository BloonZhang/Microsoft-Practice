# A variation on anagrams
# 1 point

import sys
import re


def main():
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

  # +++++ Begin code +++++
  # Start by reading the line
  for line in inputFile:
    # Regular expression: Find the two input words
    # Note: Input is assumed to be in the correct format
    inputWords = re.search(r"\"(.*?)\".*?\"(.*?)\"", line)
    if not inputWords:
      print("fail")
      continue

    # At this point, we've gotten the two input words
    # Let's normalize and sort each one, and see if they match exactly
    word1 = inputWords.group(1).replace(" ", "").lower()
    word1 = sorted(word1)
    word2 = inputWords.group(2).replace(" ", "").lower()
    word2 = sorted(word2)
    if word1 == word2:
      print("Valid Pattern")
    else:
      print("Invalid Pattern")

  # Done with the program
  pass


if __name__ == '__main__':
  main()
