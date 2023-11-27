from collections import deque
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    c,_,a=input().strip(),int(input()),deque(eval(input().strip()))
    f=r=1
    for i in c:
        if i=='R':r=-r;continue
        if not a:f=0;print('error');break
        if r<0:a.pop()
        else:a.popleft()
    if f:print(f'[{",".join(map(str,list(a)[::r]))}]')