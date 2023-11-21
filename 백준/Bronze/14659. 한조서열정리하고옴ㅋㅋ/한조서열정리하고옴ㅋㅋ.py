n=int(input())
a=[*map(int,input().split())]
m,s,c=0,0,0
for i in a:
    if i>c: m,s,c=max(m,s),0,i
    else: s+=1
print(max(m,s))