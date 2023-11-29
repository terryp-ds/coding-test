def f(d,p,q):
    if not d%p*d%q:return d
    if p<q:p,q=q,p
    a=d//p
    n=p*a+p
    for i in range(a,-1,-1):
        v,m=divmod(d-p*i,q)
        if not m: return d
        x=p*i+v*q+q
        if n==x:break
        n=min(n,x)
    return n
print(f(*map(int,input().split())))