from itertools import product

n,m = map(int, input().split())
prod = sorted(product(range(1, n+1), repeat=m))
    
for p in prod:
    print(*p, sep=' ')
