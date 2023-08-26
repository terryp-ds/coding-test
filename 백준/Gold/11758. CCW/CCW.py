def ccw(a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - b[0]*a[1] - c[0]*b[1] - a[0]*c[1])

s = [list(map(int, input().split())) for _ in range(3)]
ans = ccw(s[0],s[1],s[2])

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)