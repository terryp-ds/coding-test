from collections import Counter
import sys
input = sys.stdin.readline
c=Counter([int(input()) for _ in range(int(input()))])
print(sorted(sorted(c.items()),key=lambda x:x[1],reverse=True)[0][0])