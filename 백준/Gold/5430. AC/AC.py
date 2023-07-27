from collections import deque
import sys
n=int(input())
for i in range(n):
    c,m,a=[sys.stdin.readline().rstrip() for j in range(3)]
    c,m,a=deque(c),int(m),a[1:-1].split(',')
    a=deque(a)
    r=0
    f=1
    if m==0:
        a=[]
    for s in c:
        if s=='R':
            r=1-r
        else:
            if len(a)<1:
                f=0
                print("error")
                break
            else:
                if r:
                    a.pop()
                else:
                    a.popleft()
    if f:
        if r:
            a=list(a)[::-1]
        print('['+','.join(a)+']')