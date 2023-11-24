input()
a=[*map(int,input().split())]
b,c=map(int,input().split())
print(sum([max(i-b,0)//c+((i-b>0)*((i-b)%c)>0)+1 for i in a]))