import sys
input()
a=set([int(i) for i in sys.stdin.readline().strip().split()])
input()
b=[int(i) for i in sys.stdin.readline().strip().split()]
for i in b:
    if i in a:
        print(1)
    else:
        print(0)
