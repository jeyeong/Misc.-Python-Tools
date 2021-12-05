"""
Converts a text file (or redirected stream) to proper,
upper, lower, alternating, or random case.
"""

import sys
from random import random


def proper(string):
  """
  Converts string to proper case.
  """
  def propercase(sentence):
    n = len(sentence)
    ptr = 0
    while sentence[ptr].isspace():
      ptr += 1
    if ptr >= n - 1: proper_cased.append(sentence)
    else: proper_cased.append(sentence[: ptr + 1].upper() + sentence[ptr + 1:].lower())

  breaking_punctuation = ['.', '!', '?', '"']
  proper_cased = []
  ptr = 0
  prev_ptr = 0
  while ptr < len(string):
    if string[ptr] in breaking_punctuation:
      sentence = string[prev_ptr: ptr + 1]
      propercase(sentence)
      prev_ptr = ptr + 1
    ptr += 1
  propercase(string[prev_ptr:])    # remaining part of the string
  return ''.join(proper_cased)


def alternating(string):
  """
  Converts string to alternating case. e.g., abcd -> AbCd
  """
  alternating = []
  ptr = 0
  upper = True
  while ptr < len(string):
    if string[ptr].isalnum():
      alternating.append(string[ptr].upper() if upper else string[ptr].lower())
      upper = not upper
    else:
      alternating.append(string[ptr])
    ptr += 1
  return ''.join(alternating)


def random_cased(string):
  """
  Converts string to random case.
  """
  random_cased = []
  ptr = 0
  while ptr < len(string):
    if random() > 0.5: random_cased.append(string[ptr].upper())
    else: random_cased.append(string[ptr].lower())
    ptr += 1
  return ''.join(random_cased)


def convertcase(string, mode=0):
  """
  Modes: 0=proper, 1=upper, 2=lower, 3=alternating, 4=random
  """
  if mode == 0:
    return proper(string)
  elif mode == 1:
    return string.upper()
  elif mode == 2:
    return string.lower()
  elif mode == 3:
    return alternating(string) 
  elif mode == 4:
    return random_cased(string)
  else:
    print(f'Error: Mode not recognized.')
    quit()


if __name__ == '__main__':
  if len(sys.argv) == 1:
    # Stream
    sys.stdout.write(
      convertcase(sys.stdin.read())
    )
  else:
    # File
    try:
      filename = sys.argv[1]
      input_ = open(filename, 'r')
      mode = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    except FileNotFoundError:
      print(f'Error: {sys.argv[1]} is not a valid file.')
    except ValueError:
      print(f'Error: {sys.argv[2]} is not a valid mode.')
    else:
      with open('output.txt', 'w') as output:
        output.write(convertcase(input_.read(), mode))
      input_.close()
