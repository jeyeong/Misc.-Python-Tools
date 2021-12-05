# Case Converstion

Demonstrates file functions from *open()* interface. Accepts a text file (or a redirected stream) and converts the string to proper (mode=0), upper (mode=1), lower (mode=2), alternating (mode=3), or random (mode=4) case.

Usage:
1. **Text file:** *python convertcase.py \<filename\> \<mode\>*
2. **Pipe:** *\<first command\> | python convertcase.py*

Examples:
1. *python convertcase.py sample.txt*
2. *type sample.txt | python convertcase.py*
