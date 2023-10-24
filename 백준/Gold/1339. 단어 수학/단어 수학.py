a=[input() for _ in range(int(input()))]
d={}
for s in a:
    for i,x in enumerate(s):
        if x not in d: d[x]=0
        d[x]+=10**(len(s)-i-1)
d=[i[1] for i in sorted(d.items(),key=lambda x:x[1],reverse=True)]
c,m=0,9
for n in d: c+=m*n; m-=1
print(c)