s=input().split()
print(*[sum(map(int,[i.replace(a[0],a[1]) for i in s])) for a in ['65','56']])