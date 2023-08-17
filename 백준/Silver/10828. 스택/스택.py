import sys
input = sys.stdin.readline

s = []

for _ in range(int(input())):
    
    c = input().rstrip().split()

    if c[0] == 'push':
        s.append(c[1])

    elif c[0] == 'pop':
        print(s.pop() if s else -1)

    elif c[0] == 'size':
        print(len(s))

    elif c[0] == 'empty':
        print(int(len(s)==0))

    else:
        print(s[-1] if s else -1)
