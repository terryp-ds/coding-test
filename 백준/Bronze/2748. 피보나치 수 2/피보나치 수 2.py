d=[0,1]
for i in range(int(input())-1):d+=[d[-1]+d[-2]]
print(d[-1])