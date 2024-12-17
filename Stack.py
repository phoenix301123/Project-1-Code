#PYTHON 
import sys
stack = []
for line in sys.stdin:
    line = line.strip()
    if line == '#':
        break
    elif line.startswith('PUSH'):
        i, value = line.split()
        stack.append(int(value))
    elif line == 'POP':
        if stack:
            print(stack.pop())
        else:
            print("NULL")
            
