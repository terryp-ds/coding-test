import sys

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]

ans = [0]
ans2 = []

for row in arr:
    
    for idx, num in enumerate(row):
        
        if idx == 0:
            ans2.append(ans[idx]+num)
            
        elif idx == len(row)-1:
            ans2.append(ans[-1]+num)
            
        else:
            ans2.append(max(ans[idx-1], ans[idx])+num)
            
    ans = ans2
    ans2 = []
        
print(max(ans))
