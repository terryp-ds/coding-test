while 1:
 n,a,w=input().split()
 if n=='#':break
 print(n,['Junior','Senior'][int(a)>17 or int(w)>79])
