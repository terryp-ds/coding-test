import sys
input=sys.stdin.readline
dy,dx=[-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]
while 1:
 w,h=map(int,input().split())
 if w+h==0:break
 a=[list(map(int,input().split())) for _ in range(h)]
 n=0
 for i in range(h):
  for j in range(w):
   if a[i][j]==0:continue
   a[i][j]=0
   n+=1
   q=[(i,j)]
   while q:
    y,x=q.pop()
    for k in range(8):
     ny,nx=y+dy[k],x+dx[k]
     if 0<=ny<h and 0<=nx<w and a[ny][nx]:
      a[ny][nx]=0
      q+=[(ny,nx)]
 print(n)