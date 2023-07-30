import sys

input = sys.stdin.readline

s = set()

for i in range(int(input())):
    c = input().rstrip()
    if c != 'all' and c != 'empty':
        c,n = c.split()
        n = int(n)

    if c == 'add':
        s.add(n)

    elif c == 'remove':
        if n in s:
            s.remove(n)

    elif c == 'check':
        print(int(n in s))

    elif c == 'toggle':
        if n in s:
            s.remove(n)
        else:
            s.add(n)

    elif c == 'all':
        s = set(range(1, 21))

    else:
        s = set()
