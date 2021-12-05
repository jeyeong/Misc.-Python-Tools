"""
Split and interactively page a string (stdin, for stream redirection)
or file of text
"""

import sys

OKBLUE = '\033[94m'
ENDC = '\033[0m'

def getreply():
  """
  read a reply key from an interactive user
  even if stdin redirected to a file or pipe
  """
  inputstr = f'{OKBLUE}More?{ENDC}'
  if sys.stdin.isatty():
    return input(inputstr).encode()
  else:
    if sys.platform[:3] == 'win':
      import msvcrt
      for ch in inputstr:
        msvcrt.putch(ch.encode())
      key = msvcrt.getche()
      msvcrt.putch(b'\n')
      return key
    else:
      assert False, 'platform not supported'

def more(text, numlines=15):
  """
  splits a string of text (by \n) and
  interactively pages it with user input 
  """
  lines = text.splitlines()
  while lines:
    chunk = lines[:numlines]
    lines = lines[numlines:]
    for line in chunk:
      print(line)
    if lines and getreply() not in [b'', b'y', b'Y', b'\r']:
      break

if __name__ == '__main__':
  if len(sys.argv) == 1:
    more(sys.stdin.read(), 10)
  else:
    more(open(sys.argv[1]).read(), 10)
