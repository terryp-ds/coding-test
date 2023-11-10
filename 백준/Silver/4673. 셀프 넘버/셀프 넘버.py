s=set([i+sum(map(int,list(str(i)))) for i in range(1,10001)])
for i in range(1,10001):
    if i not in s: print(i)