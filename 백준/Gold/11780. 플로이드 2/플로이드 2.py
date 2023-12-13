import sys
input=sys.stdin.readline
n=int(input())
f=float('inf')
v=[[f]*n for _ in range(n)]
g=[[-1]*n for _ in range(n)]
for _ in range(int(input())):
 s,e,w=map(int,input().split())
 s,e=s-1,e-1
 v[s][e]=min(v[s][e],w)
 g[s][e]=s
for m in range(n):
 v[m][m]=0
 for l in range(n):
  for r in range(n):
   a=v[l][m]+v[m][r]
   if a<v[l][r]:
    v[l][r],g[l][r]=a,g[m][r]
for r in v:print(*[[0,i][i<f] for i in r])
for i in range(n):
 for j in range(n):
  if v[i][j] in (0,f):print(0);continue
  a=[]
  e=j
  while e!=i:a+=[e+1];e=g[i][e]
  print(*[len(a)+1,i+1,*a[::-1]])