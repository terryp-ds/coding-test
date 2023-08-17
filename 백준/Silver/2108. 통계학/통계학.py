from collections import Counter
import sys
input = sys.stdin.readline

n=int(input())
s=sorted(int(input()) for i in range(n))

print(int(round(sum(s)/n, 0)))
print(s[n//2])
    
c=sorted(Counter(s).items(),key=lambda x:(x[1], x[0]))
c=[i for i in c if i[1]==c[-1][1]]

print(c[0][0] if len(c) == 1 else c[1][0])    
print(s[-1]-s[0])
