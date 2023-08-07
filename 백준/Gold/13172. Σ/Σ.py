from functools import reduce
from math import gcd

d = 1000000007
m = int(input())

def pow(x, n):
    if n == 1:
        return x % d
    elif n % 2:
        return x * pow(x, n-1) % d
    else:
        p = pow(x,n//2)
        return p * p % d

def get_lcm(x,y):
    return x*y//gcd(x,y)


dice = [list(map(int, input().split())) for _ in range(m)]
lcm = reduce(get_lcm, [x[0] for x in dice])

s = sum([y*lcm//x for x,y in dice])
g = gcd(s, lcm)
a, b = s//g, lcm//g

print(a*pow(b, d-2) % d)
