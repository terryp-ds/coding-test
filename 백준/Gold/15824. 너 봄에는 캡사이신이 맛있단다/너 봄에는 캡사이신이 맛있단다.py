d=10**9+7
n=int(input())
a=sorted([*map(int,input().split())])
def s(i):
    if i<2: return 2**i
    else: return (s(i%2)%d)*((s(i//2)**2)%d)
print(sum([a[i]*((s(i)-1)-(s(n-1-i)-1)) for i in range(n)])%d)