from itertools import product
n = int(input())

d1 = [i**2 for i in range(1, int(50000**0.5))]

if n in d1:
    print(1)

else:
    d2 = set([i+j for i,j in product(d1, repeat=2) if i+j <= 50000])

    if n in d2:
        print(2)

    else:
        f = 1
        
        for i in d1:
            if n-i in d2:
                print(3)
                f = 0
                break

        if f:
            print(4)
