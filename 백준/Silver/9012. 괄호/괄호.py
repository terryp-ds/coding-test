import sys
input = sys.stdin.readline

n=int(input())
c=[input().strip() for i in range(n)]

for i in c:
    a=[]
    f=1
    for j in i:
        if j == '(':
            a.append(0)
        else:
            if not a:
                print('NO')
                f=0
                break
            else:
                a.pop()
    if f:
        if a:
            print('NO')
        else:
            print('YES')