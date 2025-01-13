_=input()
s=set(map(int,input().split()))
_=input()
print(*[int(x in s) for x in [*map(int,input().split())]])