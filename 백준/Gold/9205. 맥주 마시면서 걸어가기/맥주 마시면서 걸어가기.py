from collections import deque
import sys
input=sys.stdin.readline
for _ in range(int(input())):
 g=[]
 v={}
 for _ in range(int(input())+2):g+=[[*map(int,input().split())]]
 q=deque([g[0]])
 v[(g[0][0],g[0][1])]=1
 while q:
  x,y=q.popleft()
  if [x,y]==g[-1]:break
  for (a,b) in g:
   if (a,b) not in v and abs(x-a)+abs(y-b)<=1000:
    v[(a,b)]=1
    q+=[(a,b)]
 print(['sad','happy'][(g[-1][0],g[-1][1]) in v])