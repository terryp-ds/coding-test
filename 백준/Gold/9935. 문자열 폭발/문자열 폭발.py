s,p=input(),input()
n=len(p)
q=[]
i=0
while i<len(s):
 q+=[s[i]]
 if len(q)>=n and ''.join(q[-n:])==p: 
  for _ in range(n):q.pop()
 i+=1
print(''.join(q) if q else 'FRULA')