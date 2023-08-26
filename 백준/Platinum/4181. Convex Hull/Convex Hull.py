import sys
input = sys.stdin.readline

def ccw(a,b,c):
    return ((b[0]-a[0]) * (c[1]-a[1]) - (b[1]-a[1]) * (c[0]-a[0])) >= 0

def convex_hull(p):
    stack = []

    for c in p:

        while len(stack) > 1:
            a,b = stack[-2], stack[-1]

            if ccw(a,b,c):
                break

            stack.pop()

        stack.append(c)

    return stack

p = []

for _ in range(int(input())):
    x,y,c=input().split()
    if c == 'Y':
        p.append((int(x),int(y)))

p.sort()

u,l = convex_hull(p)[:-1], convex_hull(p[::-1])[:-1]

print(len(u)+len(l))

for c in u+l:
    print(*c)