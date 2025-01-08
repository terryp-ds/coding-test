p=[350.34,230.90,190.55,125.30,180.90]
for _ in range(int(input())):
 a=[*map(int,input().split())]
 print(f'${sum([x*y for x,y in zip(a,p)]):.2f}')