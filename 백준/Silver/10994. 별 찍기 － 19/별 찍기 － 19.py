n=int(input())
m=4*n-3
for i in range(m):
    if i>m//2:i=m-i-1
    if i&1: print(*['*' if ~j&1 & ~(i<=j<m-i)  else ' ' for j in range(m)], sep='')
    else: print(*['*' if (~j&1) | (i<=j<m-i) else ' ' for j in range(m)], sep='')