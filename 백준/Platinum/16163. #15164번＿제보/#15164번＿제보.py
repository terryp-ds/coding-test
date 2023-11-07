d='#'
s=d+d.join(list(input()))+d
n=len(s)
a=[0]*n 
r,p=0,0
for i in range(n):
    if i<=r: a[i] = min(a[2*p-i], r-i)
    while i-a[i]-1>=0 and i+a[i]+1<n and s[i-a[i]-1]==s[i+a[i]+1]:
        a[i]+=1
    if r<i+a[i]:
        r=i+a[i]
        p=i
print(sum([(i+1)//2 for i in a]))