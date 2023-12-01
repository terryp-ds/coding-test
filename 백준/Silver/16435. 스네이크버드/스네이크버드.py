n,l=map(int,input().split())
a=sorted([*map(int,input().split())])
i=0
while i<n and a[i]<=l+i:i+=1
print(l+i)