from collections import *
s=input()
c=Counter(s)
d=[i%2 for i in c.values()]
m=sum(d)
if len(s)%2!=m:print("I'm Sorry Hansoo");exit()
if m:
 x=list(c.keys())[d.index(1)]
 c[x]-=1
else:x=''
s=''
for k,v in sorted(c.items()): s+=k*(v//2)
print(s+x+s[::-1])