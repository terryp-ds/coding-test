a=[[1,0],[0,1]]
for i in range(2,41): a+=[[a[i-2][0]+a[i-2][1],a[i-1][0]+a[i-1][1]]]
for _ in range(int(input())): print(*a[int(input())])