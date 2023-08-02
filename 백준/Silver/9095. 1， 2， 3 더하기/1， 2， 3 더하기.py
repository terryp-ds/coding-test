import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a,b,c = 1,2,4

    if n < 3:
        print([1,2,4][n-1])

    else:
        for _ in range(n-3):
            a,b,c = b,c,a+b+c

        print(c)