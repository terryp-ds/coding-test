n=int(input())
a=[*map(int,input().split())]
s=[1]*n
for i in range(1,n):
 for j in range(0,i):
  if a[i]>a[j] and s[i]<s[j]+1:s[i]=s[j]+1
print(max(s))