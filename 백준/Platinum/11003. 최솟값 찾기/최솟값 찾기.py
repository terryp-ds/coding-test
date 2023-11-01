from collections import deque
n,l=map(int,input().split())
a=[*map(int,input().split())]
q=deque([])
m=[]
for i in range(n):
    while q and q[-1][1] >= a[i]: q.pop()
    while q and q[0][0] < i-l+1: q.popleft()
    q+=[(i,a[i])]
    m+=[(q[0][1])]
print(*m)