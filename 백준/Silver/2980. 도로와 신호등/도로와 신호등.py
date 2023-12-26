n,l=map(int,input().split())
q=[[*map(int,input().split())] for _ in range(n)]
i,c,t=0,0,0
while i<n:
 t+=q[i][0]-c
 t+=max(0,q[i][1]-(t%(q[i][1]+q[i][2])))
 c=q[i][0]
 i+=1
print(t+l-c)