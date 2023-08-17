import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)

else:
    arr = [int(input()) for _ in range(n)]
    cut = int(n*0.15+0.5)

    print(int(sum(sorted(arr)[cut:n-cut])/(n-2*cut)+0.5))
