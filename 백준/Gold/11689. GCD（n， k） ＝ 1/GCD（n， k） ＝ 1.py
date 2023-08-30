n = int(input())
a = n
    
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        while n % i == 0:
            n /= i
            
        a -= a / i

if n > 1:
    a -= a / n

print(int(a))