from collections import Counter
import sys
input = sys.stdin.readline

n=int(input())
s=sorted(int(input()) for i in range(n))
c=Counter(s).most_common(2)*2

print(int(round(sum(s)/n, 0)))
print(s[n//2])
print(c[1][0] if c[0][1] == c[1][1] else c[0][0])    
print(s[-1]-s[0])
