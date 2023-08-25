x=int(input())
a=64
c=0
while x:
    if a <= x:
       x -= a
       c += 1
    a >>= 1
        
print(c)
