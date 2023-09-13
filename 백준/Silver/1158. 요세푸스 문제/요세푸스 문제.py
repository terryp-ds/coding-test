from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
q=deque(range(1,n+1))
a=[]
while q:
    q.rotate(-k+1)
    a.append(str(q.popleft()))
print(f'<{", ".join(a)}>')