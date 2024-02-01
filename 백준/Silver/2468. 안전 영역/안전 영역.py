n=int(input())
a=[[*map(int,input().split())] for _ in range(n)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
m,t=1,1
s=max(map(max,a))
while t<=s:
 v=[[0]*n for _ in range(n)]
 c=0
 for i in range(n):
  for j in range(n):
   if a[i][j]<=t or v[i][j]:continue
   q=[(i,j)]
   v[i][j]=1
   c+=1
   while q:
    y,x=q.pop()
    for k in range(4):
     ny,nx=y+dy[k],x+dx[k]
     if 0<=ny<n and 0<=nx<n and v[ny][nx]==0 and a[ny][nx]>t:
      q+=[(ny,nx)]
      v[ny][nx]=1
 m=max(m,c)
 t+=1
print(m)