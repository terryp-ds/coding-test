for _ in range(int(input())):
 s=0
 for _ in range(int(input())):
  n,q,p=input().split()
  s+=int(q)*float(p)
 print(f'${s:.2f}')