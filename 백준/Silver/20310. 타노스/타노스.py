s=list(input())
n,m=[s.count(x)//2 for x in '10']
for i in range(n):s.remove('1')
s=s[::-1]
for i in range(m):s.remove('0')
print(*s[::-1],sep='')