# Brainfuck Interpreter in Python
This is a Brainfuck language interpreter written in Python. Memory bytes are simulated using dictionary.

Usage:
- `python brainfuck.py` opens up a REPL
- `python brainfuck.py [filename.bf]` runs the target file
- `cat [filename.bf] | python brainfuck.py` works as well
- `python brainfuck.py < [filename.bf]` works as well

Note:
- Each statement in the REPL has a separate enviroment, i.e. dictionary
- "[" and "]" matching are not checked
- To learn more about brainfuck, look at the hello world source file
