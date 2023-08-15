import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b = find(a),find(b)

    if a < b:
        parent[b] = a

    elif a > b:
        parent[a] = b

n,m = map(int, input().split())

parent = [i for i in range(n+1)]
s = ['no', 'yes']

for _ in range(m):
    o,a,b = map(int, input().split())

    if o == 0:
        union(a,b)
    else:
        print(s[find(a) == find(b)])
