n=int(input())
a=[*map(int,input().split())]
d=sorted(dict(zip(range(n),a)).items(),key=lambda x:x[1])
z=sorted(dict(zip(d,range(n))).items())
print(*[x[1] for x in z])