a,b=map(int,input().split())
p,q=a,b
while a%b:a,b=b,a%b
print(p*q//b)