input()
m,s,c=0,0,0
for i in [*map(int,input().split())]:
 if i>c:m,s,c=max(m,s),0,i
 else:s+=1
print(max(m,s))