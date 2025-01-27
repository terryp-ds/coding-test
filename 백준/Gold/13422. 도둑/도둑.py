from collections import deque
for _ in range(int(input())):
 n,m,k=map(int,input().split())
 a=[*map(int,input().split())]
 q=deque(a[:m])
 a=a[m:]+a[:m-1]
 a=deque(a)
 s=sum(q)
 d=int(s<k)
 while a and n!=m:
  p,x=q.popleft(),a.popleft()
  s=s-p+x
  q+=[x]
  if s<k:d+=1
 print(d)