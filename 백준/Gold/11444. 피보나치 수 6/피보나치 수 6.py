d = 1000000007

def matmul(m1, m2):
    new_m = []

    for r in m1:
        new_r = []

        for i, _ in enumerate(r):
            new_r.append(sum(map(lambda x,y:x*y, r, [r2[i] for r2 in m2])) % d)

        new_m.append(new_r)
        
    return new_m

def power(x, n):
    if n == 1:
        return x
    elif n % 2:
        return matmul(x, power(x, n-1))
    else:
        p = power(x,n//2)
        return matmul(p,p)

print(power([[1,1],[1,0]], int(input()))[0][1])
