from math import prod
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    dic = {}

    for _ in range(int(input())):
        v,k = input().rstrip().split()

        if k not in dic:
            dic[k] = []

        dic[k].append(v)

    print(prod(map(lambda x: len(x)+1, dic.values()))-1)
