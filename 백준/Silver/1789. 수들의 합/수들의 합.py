n=int(input())
k=int((2*n)**.5)
if k**2+k > n*2: k-=1
print(k)