import sys
input = sys.stdin.readline

n,m = map(int, input().split())
t = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(m)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b = find(a), find(b)

    if a<b:
        parent[b] = a

    elif a>b:
        parent[a] = b

if not t[0]:
    print(m)

else:
    parent = [i for i in range(n+1)]

    for i in t[1:]:
        parent[i] = 0

    for party in parties:
        for i in range(party[0]-1):
            union(party[i+1], party[i+2])

    cnt = 0

    for party in parties:
        f = 1

        for i in range(party[0]):
            if not find(party[i+1]):
                f = 0
                break

        if f:
            cnt += 1

    print(cnt)