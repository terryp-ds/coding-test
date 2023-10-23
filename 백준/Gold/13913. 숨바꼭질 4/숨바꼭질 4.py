from collections import deque
n,k=map(int,input().split())
q=deque([n])
v={n:-1}
while q:
    c=q.popleft()
    if c==k: break
    for x in [2*c,c+1,c-1]:
        if 0<=x<100001 and x not in v:
            v[x]=c
            q.append(x)
a=deque([k])
while c!=n:
    a.appendleft(v[c])
    c=v[c]
print(len(a)-1)
print(*a)