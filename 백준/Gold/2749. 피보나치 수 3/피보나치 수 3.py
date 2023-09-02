d = 1000000
def mul(m1,m2):
    m=[]
    for r in m1:
        mr=[]
        for i, _ in enumerate(r):
            mr.append(sum(map(lambda x,y:x*y,r,[r2[i] for r2 in m2]))%d)
        m.append(mr)
    return m
def po(x,n):
    if n==1:
        return x
    elif n%2:
        return mul(x,po(x,n-1))
    else:
        p=po(x,n//2)
        return mul(p,p)
print(po([[1,1],[1,0]],int(input()))[0][1])