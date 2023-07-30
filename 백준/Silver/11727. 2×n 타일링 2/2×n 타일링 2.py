n = int(input())
dic = {1:1, 2:3}

def fib(k):
    if k not in dic:
        dic[k] = fib(k-1) + fib(k-2) * 2
    return dic[k]

print(fib(n) % 10007)
