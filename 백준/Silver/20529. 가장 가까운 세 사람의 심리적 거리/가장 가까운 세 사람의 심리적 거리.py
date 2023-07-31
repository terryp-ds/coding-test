from collections import Counter
from itertools import combinations
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = input().rstrip().split()

    if n >= 33:
        print(0)

    else:
        counter = Counter(arr)

        if max(counter.values()) == 3:
            print(0)

        else:
            comb = set(combinations(arr, 3))
            min_score = 12

            for c in comb:
                score = 0

                for x,y in [[c[0], c[1]], [c[1], c[2]], [c[2], c[0]]]:
                    score += sum([x[i]!=y[i] for i in range(4)])

                min_score = min(min_score, score)

            print(min_score)
