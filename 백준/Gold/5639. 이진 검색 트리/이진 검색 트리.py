import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

arr = []

while 1:                            
    try:
        arr.append(int(input()))
    except:
        break
        
def post_order(s, e):
    if s > e:
        return
    m = e + 1

    for i in range(s+1, e+1):
        if arr[s] < arr[i]:
            m = i
            break

    post_order(s+1, m-1)
    post_order(m, e)
    print(arr[s])

post_order(0, len(arr)-1)
