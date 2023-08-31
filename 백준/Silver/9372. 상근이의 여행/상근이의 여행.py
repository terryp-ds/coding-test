import sys
I = sys.stdin.readline
for _ in range(int(I())):
    n,m = map(int, I().split())
    print(n-1)
    _ = [I() for _ in range(m)]