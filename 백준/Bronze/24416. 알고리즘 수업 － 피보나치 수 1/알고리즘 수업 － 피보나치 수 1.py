n = int(input())

fib_dict = {1:1, 2:1}

def fib(k):
    if k not in fib_dict:
        fib_dict[k] = fib(k-1)+fib(k-2)
    return fib_dict[k]


print(fib(n), n-2)