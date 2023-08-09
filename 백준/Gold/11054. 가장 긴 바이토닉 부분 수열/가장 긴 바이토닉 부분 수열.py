import sys
input = sys.stdin.readline

def lis(arr):
    n = len(arr)

    lis = [1]*n

    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j] + 1

    return lis

    
n = int(input())
arr = list(map(int, input().split()))

arr2 = [i+j for i,j in zip(lis(arr), lis(arr[::-1])[::-1])]

print(max(arr2)-1)
