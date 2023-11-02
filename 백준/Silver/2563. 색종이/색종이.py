a=[0]*10000
for i in range(int(input())):
    x,y=map(int,input().split())
    for w in range(x,x+10):
        for s in range(y,y+10): a[w*100+s]=1
print(sum(a))