from math import factorial as f
n=int(input())
print(f(n+9) // (f(9)*f(n)) % 10007)