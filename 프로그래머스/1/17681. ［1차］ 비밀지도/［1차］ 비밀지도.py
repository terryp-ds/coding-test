def solution(n, arr1, arr2):
    arr1 = [str(bin(i)[2:]).zfill(n) for i in arr1]
    arr2 = [str(bin(i)[2:]).zfill(n) for i in arr2]
    
    arr = []
    
    for r1,r2 in zip(arr1,arr2):
        row = [' ' if i==j=='0' else '#' for i,j in zip(r1,r2)]
        arr.append(''.join(row))

    return arr