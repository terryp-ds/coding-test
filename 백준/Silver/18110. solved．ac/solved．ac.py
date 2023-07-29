import sys

n = int(input())

if n == 0:
    print(0)

else:
    arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
    cut = int(n*0.15+0.5)

    print(int(sum(sorted(arr)[cut:len(arr)-cut])/(len(arr)-2*cut)+0.5))
