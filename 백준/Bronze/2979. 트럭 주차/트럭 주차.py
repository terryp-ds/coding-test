w=[*map(int,input().split())]
a=[[*map(int,input().split())] for _ in range(3)]
s=[]
for i in range(3):
    for j in range(2):
        s.append((a[i][j],'abc'[i]))
s.sort()
d=set()
n,t=0,0
for y,x in s:
    c=len(d)
    if n: t+=(y-n)*w[c-1]*c
    if x in d: d.remove(x)
    else: d.add(x)
    n=y
print(t)