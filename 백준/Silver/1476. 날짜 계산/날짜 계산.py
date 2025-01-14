e,s,m=map(int,input().split())
for i in range(1,7981):
 if ((i-1)%15+1,(i-1)%28+1,(i-1)%19+1)==(e,s,m):break
print(i)