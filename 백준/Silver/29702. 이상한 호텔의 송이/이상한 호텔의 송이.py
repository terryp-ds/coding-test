import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    while n > 0:
        d = n.bit_length()
        print(str(d)+str(n-(1<<(d-1))+1).zfill(18))
        n>>=1