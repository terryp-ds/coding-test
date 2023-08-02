import sys
input = sys.stdin.readline

def lcm(p,q):
    a,b = p,q
    
    while q != 0:
        p,q = q, p%q
        
    return a*b//p

for _ in range(int(input())):
    m,n,x,y = map(int, input().split())

    if x == y == 1:
        print(1)

    else:
        i = 0
        l = lcm(m,n)

        if m == 1 or n == 1:
            if m == 1:
                print(y if y <= n else -1)
            else:
                print(x if x <= m else -1)
                
        else:
            if m != n:
                while i < l:
                    if (i+y-1) % m +1 == x:
                        break
                    else:
                        i += n

                print(i+y if i < l else -1)

            else:
                if x == y:
                    print(x if x <= m else -1)
                    
                else:
                    print(-1)
