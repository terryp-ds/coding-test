def ccw(a,b,c): return ((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))>0
def cv(a):
    q=[]
    for c in a:
        while len(q)>1:
            a,b=q[-2:]
            if ccw(a,b,c):break
            q.pop()
        q+=[c]
    return len(q)
n=int(input())
a=sorted([[*map(int,input().split())] for _ in range(n)])
print(cv(a)+cv(a[::-1])-2)