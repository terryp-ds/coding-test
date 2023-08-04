from functools import reduce

a,b,c = map(int, input().split())

b2 = bin(b)[2:][::-1]

d = {0:a%c}

for i in range(1, len(b2)):
    d[i] = d[i-1]**2 % c

print(reduce(lambda x,y:x*y%c, [d[i] for i,j in enumerate(b2) if int(j)]) % c)

