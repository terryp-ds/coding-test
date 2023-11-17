input()
a=[*map(int,input().split())]
s=sorted(set(a))
d=dict(zip(s,range(len(s))))
print(*[d[i] for i in a])