k = int(input())
w,h = [],[]
a = []

for _ in range(6):
    d, e=map(int, input().split())
    if d < 3:
        w.append(e)
    else:
        h.append(e)
    a.append(((d-1)//2,e))

n,m = max(w),max(h)
i,j = a.index((0,n)), a.index((1,m))

if (i+1)%6 != j:
    i = j
    
print((n*m - a[i-2][1]*a[i-3][1])*k)
