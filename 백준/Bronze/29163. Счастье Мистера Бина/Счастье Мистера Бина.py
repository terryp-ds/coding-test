n=int(input())
a=[*map(int,input().split())]
print(['Sad','Happy'][sum([x%2 for x in a])<n/2])