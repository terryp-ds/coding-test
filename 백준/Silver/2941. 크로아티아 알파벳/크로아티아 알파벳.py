from re import findall
x=input()
d=['c=','c-','dz=','d-','lj','nj','s=','z=']
a=[]
for s in d:
    a.extend(findall(s,x))
print(len(x)-len(a))