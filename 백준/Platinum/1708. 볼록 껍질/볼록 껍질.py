def ccw(a,b,c):
    return ((b[0]-a[0]) * (c[1]-a[1]) - (b[1]-a[1]) * (c[0]-a[0])) > 0

def convex_hull(coords):
    stack = []

    for c in coords:

        while len(stack) > 1:
            a,b = stack[-2], stack[-1]

            if ccw(a,b,c):
                break

            stack.pop()

        stack.append(c)

    return len(stack)

n = int(input())
coords = sorted([list(map(int, input().split())) for _ in range(n)])
print(convex_hull(coords)+convex_hull(coords[::-1])-2)