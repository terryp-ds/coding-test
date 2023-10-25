import sys
input=sys.stdin.readline
a=sorted([int(input()) for _ in range(int(input()))], reverse=True)
s,n,m=0,0,0
for i in a:
    s+=i
    n+=1
    m=max(m,i*n)
print(m)
