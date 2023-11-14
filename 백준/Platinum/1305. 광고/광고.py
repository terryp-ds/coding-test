l,p=int(input()),input()
a=[0]*l
n,i=0,1
while i<l:
    if p[i]==p[n]:
        n+=1
        a[i]=n
        i+=1
    else:
        if n!=0: n=a[n-1]
        else:
            a[i]=0
            i+=1
print(l-a[l-1])