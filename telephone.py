# Phone number parsing
# 1 point

import sys


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


# The main program
def main():
  inputFile = openFile()
  outputFile = open("telephoneResult.txt", "w")

  # Create a dict to translate alphabet to number
  translate = {
    'a': 2,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 3,
    'f': 3,
    'g': 4,
    'h': 4,
    'i': 4,
    'j': 5,
    'k': 5,
    'l': 5,
    'm': 6,
    'n': 6,
    'o': 6,
    'p': 7,
    'q': 7,
    'r': 7,
    's': 7,
    't': 8,
    'u': 8,
    'v': 8,
    'w': 9,
    'x': 9,
    'y': 9,
    'z': 9
  }

  # Start looking through each line
  for line in inputFile:
    # The parsed phone number
    result = ""
    # In case of anything unexpected
    error = False

    for char in line:
      if not char.isalnum():
        continue

      # At this point, the character should be alphanumeric
      # If it is a letter instead of a number
      if char.isalpha():
        # Checks if the char is in the dict
        if not (char.lower() in translate):
          # it's not a good character!
          error = True
          break
        else:
          char = translate[char.lower()]
      # If it's a number
      result = result + str(char)

    # We've finished one line!
    # Let's add a one if needed
    if len(result) == 10:
      result = "1" + result

    # Now let's check for errors
    # If the number doesn't begin with a 1
    if len(result) == 11 and result[0] != "1":
      error = True
    # If the length isn't 11 digits
    elif len(result) != 11:
      error = True
    # If the syntax of the original string was incorrect
    elif line[0] == "+" and line[1] != "1":
      error = True

    # If error flag is set
    if error:
      outputFile.write("Fleshling follow-up needed\n")
    else:
      outputFile.write("+" + result + "\n")

  # Done with the program
  pass


if __name__ == '__main__':
  main()
