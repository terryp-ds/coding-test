from collections import Counter
import sys
input()
a=sorted([int(i) for i in sys.stdin.readline().strip().split()])
input()
b=[int(i) for i in sys.stdin.readline().strip().split()]

c=Counter(a)
print(' '.join([f'{c[i]}' if i in c else '0' for i in b]))