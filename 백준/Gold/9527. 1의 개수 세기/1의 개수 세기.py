def ps(n):
    if n < 1:
        return 0

    p = n.bit_length()-1
    i = 2 ** p

    if n == i:
        return p*n//2+1

    return ps(i) + ps(n-i) + n-i

a,b = map(int, input().split())
print(ps(b)-ps(a-1))