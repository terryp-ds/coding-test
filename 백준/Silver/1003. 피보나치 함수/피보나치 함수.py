import sys

input = sys.stdin.readline

n = int(input())

dict_0 = {0:0, 1:1}
dict_1 = {0:1, 1:0}

def fib_0(k):
    if k not in dict_0:
        dict_0[k] = fib_0(k-1) + fib_0(k-2)

    return dict_0[k]


def fib_1(k):
    if k not in dict_1:
        dict_1[k] = fib_1(k-1) + fib_1(k-2)

    return dict_1[k]


for _ in range(n):
    k = int(input())
    print(f'{fib_1(k)} {fib_0(k)}')
