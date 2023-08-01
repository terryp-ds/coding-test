import sys
input = sys.stdin.readline

n, target = map(int, input().split())
arr = sorted(map(int, input().split()), reverse=True)

start, end = 1, arr[0]

def cut_tree(trees, h):
    s = 0

    for i in range(n):
        
        if trees[i] < h:
            break
        
        else:
            s += trees[i]-h

    return s


while start <= end:
    mid = (start+end)//2
    cut = cut_tree(arr, mid)

    if cut < target:
        end = mid-1

    else:
        start = mid+1

print(end)
