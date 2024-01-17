import sys

chars = {'+','-','<','>','[',']','.',','}

arr = [0 for _ in range(10000)]

#file = sys.argv[1]
file = 'test.bf'

debug = 1

with open(file) as f: code = ''.join([i for i in f.read() if i in chars])

sel = 0
offset = 0

while offset < len(code):
    if debug == 2: input(f'Char: [{code[offset]}], offset: [{offset}], sel: [{sel}], arr: {'|'.join([str(i) for i in arr])}')
    try:
        char = code[offset]
        if arr[sel] == 256: arr[sel] = -255
        if arr[sel] == -256: arr[sel] = 255
        if sel < 0: sel = 0
        if debug == 1: print(char,end='')

        if char == '+': arr[sel] += 1
        if char == '-': arr[sel] -= 1
        if char == '.': print((arr[sel]),end='')
        if char == ',': arr[sel] = ord(input('')[0])
        if char == '>': sel += 1
        if char == '<': sel -= 1
        if char == '[' and arr[sel] == 0:
            offset = code.index(']',offset)-1
            if debug: print(f'\nJumped to char {code[offset]} at index {offset}')
        if char == ']' and arr[sel] != 0:
            offset = code.rindex('[',0,offset)-1
            if debug: print(f'\nLooped back to char {code[offset]} at index {offset}')
    except Exception as e: print(e)
    offset += 1







