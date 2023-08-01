import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
b = input().rstrip()
b = set(map(int, b.split()))

if n == 100:
    print(0)

elif m == 10:
    print(abs(n-100))

elif not set([int(i) for i in str(n)]).intersection(b):
    print(min(len(str(n)), abs(n-100)))

else:
    cnt = 1
    arr = []
    f = 1
    
    while f:
        arr = [n-cnt, n+cnt]
        
        for num in arr:
            if num >= 0:
                s = set([int(i) for i in str(num)])
                
                if not s.intersection(b):
                    print(min(len(str(num))+cnt, abs(n-100)))
                    f = 0
                    break
        
        cnt += 1
