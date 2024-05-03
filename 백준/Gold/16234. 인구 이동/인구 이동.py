n,l,r=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(n)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
v=[[0]*n for _ in range(n)]
def dfs(q):
 y,x=q[0]
 z=[(y,x)]
 s=a[y][x]
 c=1
 while q:
  y,x=q.pop()
  v[y][x]=1
  for i in range(4):
   ny,nx=y+dy[i],x+dx[i]
   if 0<=ny<n and 0<=nx<n and not v[ny][nx] and l<=abs(a[y][x]-a[ny][nx])<=r:
     v[ny][nx]=1
     q+=[(ny,nx)]
     z+=[(ny,nx)]
     s+=a[ny][nx]
     c+=1
 return (z,s//c) if c>1 else (0,0)

def main():
 c=0
 q,s=[],[]
 for i in range(n):
  for j in range(n):
   z,k=dfs([(i,j)])
   if z:
    c=1
    q+=[z]
    s+=[k]
 for z,k in zip(q,s):
  for y,x in z: a[y][x]=k
 return c

c=0
while main():
 c+=1
 v=[[0]*n for _ in range(n)]
print(c)