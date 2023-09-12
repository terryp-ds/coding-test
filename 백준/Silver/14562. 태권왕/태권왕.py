from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s,t=map(int,input().split())
    v={(s,t):0}
    q=deque([(s,t)])
    while q:
        s,t=q.popleft()
        if s==t:
            break
        for c in [(s*2,t+3),(s+1,t)]:
            if c[0]<=c[1] and c not in v:
                q.append(c)
                v[c]=d[(s,t)]+1
    print(v[(s,t)])
