a=[*map(int,input().strip())]
m=len(a)-1
c=[0]*10
k=0
for n in a:
    for i in range(n): c[i]+=10**m
    if m>0: k+=n*m*(10**(m-1))
    if m: c[n]+=(int(''.join(map(str,a[-m:])))+1)
    else: c[n]+=1
    c[0]-=10**m
    m-=1
print(*[i+k for i in c])