a,b=[int(i) for i in input().split()]
d=dict(zip(list(range(36)), [str(i) for i in range(10)]+list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
c=0
while 1:
    if b**c > a:
        break
    else:
        c+=1
r=[]
if c==0:
    print(d[a])
else:
    for i in range(c-1,-1,-1):
        p = a // (b**i)
        a -= p*(b**i)
        r.append(p)
    print(''.join([d[i] for i in r]))