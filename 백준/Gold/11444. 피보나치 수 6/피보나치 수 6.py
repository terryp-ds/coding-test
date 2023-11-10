d=10**9+7
def mul(x,y):
    m=[]
    for r in x:
        a=[]
        for i,_ in enumerate(r): a+=[sum(map(lambda x,y:x*y,r,[j[i] for j in y]))%d]
        m.append(a)
    return m
def pow(x,n):
    if n==1: return x
    elif n%2: return mul(x,pow(x,n-1))
    else:
        p=pow(x,n//2)
        return mul(p,p)
print(pow([[1,1],[1,0]],int(input()))[0][1])