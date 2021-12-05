# Case Converstion

Demonstrates file functions from Python's *open()* interface. Accepts a text file (or a redirected stream) and converts the string to proper, upper, lower, alternating, or random case.

Usage:
1. **Text file:** *python convertcase.py \<filename\> \<mode\>*
2. **Pipe:** *\<first command\> | python convertcase.py*

Modes:
- 0: proper (default), 1: upper, 2: lower
- 3: alternating
- 4: random

Examples:
1. *python convertcase.py sample.txt 3*
2. *type sample.txt | python convertcase.py*
