for m in range(int(input())):
 n=int(input())
 p=n**2
 a=[[*map(int,input().split())] for _ in range(p)]
 f=1
 s=set(range(1,p+1))
 for i in range(p):
  if (set(a[i])!=s) or (set([x[i] for x in a])!=s) or (set([x for y in [x[i%n*n:i%n*n+n] for x in a[i//n*n:i//n*n+n]] for x in y])!=s):
   f=0
   break
 print(f'Case #{m+1}: {["No","Yes"][f]}')