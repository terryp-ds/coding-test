n=int(input())
a=sorted([[*map(int,input().split())] for _ in range(n)],key=lambda x:x[1])
a=[i[0] for i in a]
s=[1]*n
for i in range(1,n):
 for j in range(0,i):
  if a[i]>a[j] and s[i]<s[j]+1:s[i]=s[j]+1
print(n-max(s))