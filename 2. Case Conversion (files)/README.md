# Case Converstion

Demonstrates file functions from *open()* interface. Accepts a text file (or a redirected stream) and converts the string to proper (mode=0), upper (1), lower (2), alternating (3), or random (4) case.

Usage:
1. **Text file:** *python convertcase.py \<filename\> \<mode\>*
2. **Pipe:** *\<first command\> | python convertcase.py*

Examples:
1. *python convertcase.py sample.txt 3*
2. *type sample.txt | python convertcase.py*
