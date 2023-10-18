import sys
input=sys.stdin.readline
def pw(n,k):
    if k==1: return n
    if not k%2: return pw(n,k//2)**2%q
    else: return pw(n,k//2)**2*n%q
d=4000001
q=10**9+7
a=[1]*d
for i in range(2,d): a[i]=(a[i-1]*i)%q
for _ in range(int(input())):
    n,k=map(int,input().split())
    print(a[n]*pw(a[n-k],q-2)*pw(a[k],q-2)%q)