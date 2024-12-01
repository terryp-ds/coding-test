n,m=map(int,input().split())
a,b=[0],[0]
for _ in range(n):
 x,d=input().split()
 for _ in range(int(x)):
  a+=[a[-1]+(1 if d=='R' else -1)]
for _ in range(m):
 x,d=input().split()
 for _ in range(int(x)):
  b+=[b[-1]+(1 if d=='R' else -1)]
if len(a)<len(b):
 a+=[a[-1]]*(len(b)-len(a))
else:
 b+=[b[-1]]*(len(a)-len(b))
c,z=0,1
for i in range(len(a)):
 if a[i]==b[i] and not z:
  c+=1
  z=1
 if z and a[i]!=b[i]: z=0
print(c)