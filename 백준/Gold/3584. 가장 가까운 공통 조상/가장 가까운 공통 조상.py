import sys
I = sys.stdin.readline

for _ in range(int(I())):
    n = int(I())
    g = [[] for _ in range(n+1)]

    for _ in range(n-1):
        p,c = map(int, I().split())
        g[c] = p

    a,b = map(int, I().split())
    x,y = [a],[b]
    s = set()

    while not s:
        if g[a]:
            a = g[a]

            if a:
                x.append(a)

        if g[b]:
            b = g[b]

            if b:
                y.append(b)

        s = set(x).intersection(set(y))

    print(*s)