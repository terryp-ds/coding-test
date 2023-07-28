from math import sqrt
import sys
input()
a=[int(i) for i in sys.stdin.readline().strip().split()]
c=0
for n in a:
    f=1
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            f=0
            break
    if f and n>1:
        c+=1
print(c)