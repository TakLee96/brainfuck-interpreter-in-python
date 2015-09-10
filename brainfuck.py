import sys


class Data:
    def __init__(self):
        self.dict = dict()
        self.pointer = 0

    def get(self):
        if self.pointer not in self.dict:
            self.dict[self.pointer] = 0
        return self.dict[self.pointer]

    def set(self, value):
        self.dict[self.pointer] = value

    def next(self):
        self.pointer += 1

    def prev(self):
        self.pointer -= 1 

    def inc(self):
        self.set(self.get() + 1)

    def dec(self):
        self.set(self.get() - 1)

    def input(self):
        self.set(ord(raw_input()[0]))

    def output(self):
        sys.stdout.write(chr(self.get()))

    def __repr__(self):
        return repr(self.dict)


forms = {
    "+": lambda d: d.inc(),
    "-": lambda d: d.dec(),
    "<": lambda d: d.prev(),
    ">": lambda d: d.next(),
    ",": lambda d: d.input(),
    ".": lambda d: d.output()
}


def next_matching(code, index):
    length, count = len(code), 1
    while index < length:
        if code[index] == "[":
            count += 1
        elif code[index] == "]":
            count -= 1
        if count == 0:
            return index
        index += 1


def bf_eval(data, code, index=0):
    length = len(code)
    while index < length:
        char = code[index]
        if char in forms:
            forms[char](data)
            index += 1
        elif char == "[":
            while data.get():
                bf_eval(data, code, index + 1)
            index = next_matching(code, index + 1) + 1
        elif char == "]":
            return
        else:
            index += 1


if len(sys.argv) <= 1:
    if sys.stdin.isatty():
        while True:
            code = raw_input("brainfuck> ")
            bf_eval(Data(), code)
            sys.stdout.write("\n")
    else:
        bf_eval(Data(), sys.stdin.read())
else:
    with open(sys.argv[1], 'r') as f:
        code = f.read()
        bf_eval(Data(), code)
