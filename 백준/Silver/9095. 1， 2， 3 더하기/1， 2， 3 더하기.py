d=[1,2,4]
for i in range(3,10):d+=[sum(d[i-3:i])]
for _ in range(int(input())):print(d[int(input())-1])