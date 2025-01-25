n=int(input())
for i in range(n):
 m=[input() for _ in range(4)]
 a=[list(x) for x in m]+[[m[j][k] for j in range(4)] for k in range(4)]+[[m[j][j] for j in range(4)]]+[[m[j][3-j] for j in range(4)]]
 a=[sorted(x) for x in a]
 f=''
 for t in ['O','X']:
  if (sorted(['T']+[t]*3) in a) or ([t]*4 in a):f+=t 
 if len(f)==1:print(f'Case #{i+1}: {f} won')
 if len(f)==2:print(f'Case #{i+1}: Draw') 
 if not f:
  if sum(map(lambda x:x.count('.'),m)):print(f'Case #{i+1}: Game has not completed')
  else:print(f'Case #{i+1}: Draw') 
 if i<n-1:_=input()