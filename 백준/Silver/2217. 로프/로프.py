import sys
input=sys.stdin.readline
a=sorted([int(input()) for _ in range(int(input()))], reverse=True)
n,m=0,0
for i in a:
    n+=1
    m=max(m,i*n)
print(m)