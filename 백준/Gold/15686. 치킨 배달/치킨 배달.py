from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    
    for j in range(n):
        
        if arr[i][j] == 1:
            house.append((i,j))
            
        elif arr[i][j] == 2:
            chicken.append((i,j))


min_dist = 10000

comb = combinations(chicken, m)

for c in comb:
    
    total_dist = 0
    
    for i,j in house:

        dist = 100
        
        for x,y in c:

            cdist = abs(i-x)+abs(j-y)

            dist = min(dist, cdist)

        total_dist += dist

    min_dist = min(total_dist, min_dist)

print(min_dist)
