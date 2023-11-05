def solution(park, routes):
    r,c=len(park),len(park[0])
    for y in range(r):
        x=park[y].find('S')
        if x>-1: break
    d=dict(zip('NSWE',[(-1,0),(1,0),(0,-1),(0,1)]))
    for route in routes:
        o,n=route.split()
        n=int(n)
        for i in range(1,n+1):
            ny,nx=y+d[o][0]*i,x+d[o][1]*i
            if not (0<=ny<r and 0<=nx<c) or park[ny][nx]=='X': 
                break
        else: y,x=ny,nx
    return [y,x]