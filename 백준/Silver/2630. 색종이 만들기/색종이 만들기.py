n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]

def square(arr, target):
    m = len(arr)
    
    if m == 1:
        return arr[0][0] == target
    
    else:
        
        if sum(map(sum, arr)) == [0, m*m][target]:
            return 1
        
        else:
            return sum([
                square(
                    [row[:m//2] for row in arr[:m//2]], target
                    ), 
                square(
                    [row[:m//2] for row in arr[m//2:]], target
                    ),
                square(
                    [row[m//2:] for row in arr[:m//2]], target
                    ),
                square(
                    [row[m//2:] for row in arr[m//2:]], target
                    )
                ])

print(square(maps, 0))
print(square(maps, 1))
