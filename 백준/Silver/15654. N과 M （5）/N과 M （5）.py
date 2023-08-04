from itertools import permutations
n,m = map(int, input().split())
nums = list(map(int, input().split()))

for p in sorted(permutations(nums, m)):
    print(*p, sep=' ')
