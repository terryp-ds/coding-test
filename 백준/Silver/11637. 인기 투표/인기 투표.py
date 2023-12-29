import sys
input=sys.stdin.readline
for _ in range(int(input())):
 a=[int(input()) for _ in range(int(input()))]
 m=max(a)
 if a.count(m)>1:print('no winner');continue
 print(f"{['minority','majority'][m>sum(a)//2]} winner {a.index(m)+1}")