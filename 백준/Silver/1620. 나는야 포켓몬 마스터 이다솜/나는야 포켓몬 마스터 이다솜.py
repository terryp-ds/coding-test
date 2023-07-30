import sys

input = sys.stdin.readline
m,n = map(int, input().split())
dict_1 = {}

for i in range(m):
    dict_1[i+1] = input().rstrip()

dict_2 = dict(zip(dict_1.values(), dict_1.keys()))

for _ in range(n):
    q = input().rstrip()
    print(dict_2[q] if q.isalpha() else dict_1[int(q)])