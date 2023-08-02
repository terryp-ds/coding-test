n,r,c = map(int, input().split())

s = 0

while n > 0:
    hf = 2**(n-1)
    dr, dc = (r >= hf), (c >= hf)
    s += (dr*2 + dc) * (hf**2)
    r -= hf * dr
    c -= hf * dc
    n -= 1
    

print(s+r*2+c)
