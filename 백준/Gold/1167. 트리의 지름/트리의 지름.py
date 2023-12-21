import sys
input=sys.stdin.readline
n=int(input())
g=[[] for _ in range(n+1)]
for _ in range(n):
 a=[*map(int, input().split())]
 for j in range(len(a)//2-1): g[a[j*2+1]]+=[(a[j*2+2],a[0])]
def dfs(s):
 v=[0]*(n+1)
 q=[(0,s)]
 v[s]=1
 while q:
  w,e=q.pop()
  for w2,e2 in g[e]:
   if not v[e2]:
    q+=[(w+w2,e2)]
    v[e2]+=w+w2
 return (max(v),v.index(max(v)))
print(dfs(dfs(1)[1])[0])