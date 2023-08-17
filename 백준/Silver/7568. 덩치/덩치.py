import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]
score = []

for p1 in arr:
    s = 1
    for p2 in arr:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            s += 1
    score.append(s)
    
print(*score)
