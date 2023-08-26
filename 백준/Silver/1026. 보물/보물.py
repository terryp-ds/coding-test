n=int(input())
a=0
for i,j in zip(sorted([*map(int, input().split())]), sorted([*map(int, input().split())], reverse=True)):
    a+=i*j 
print(a)