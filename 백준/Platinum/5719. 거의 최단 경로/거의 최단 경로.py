from collections import deque
import sys, heapq
input = sys.stdin.readline

def dijkstra(start,end,edges):
    hq = [(0,start)]
    dist = [float('inf')]*n
    visit = [False]*n
    while hq:
        curDist, curNode = heapq.heappop(hq)
        if visit[curNode]:
            continue
        visit[curNode] = True
            
        if curDist > dist[curNode]:
            continue
        dist[curNode] = curDist
        
        if curNode == end:
            return dist
        for toNode, toDist in edges[curNode]:
            d = curDist + toDist
            if d > dist[toNode] or not edge_check[curNode][toNode]:
                continue
            heapq.heappush(hq,(d,toNode))

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    start, end = map(int,input().split())
    edge = [[] for _ in range(n)]
    edge_reverse = [[] for _ in range(n)]
    edge_check = [[False]*(n) for _ in range(n)]
    
    for i in range(m):
        u,v,p = map(int,input().split())
        edge[u].append((v,p))
        edge_reverse[v].append((u,p))
        edge_check[u][v] = True
    
    dist1 = dijkstra(start,end,edge)
    if dist1 == None:
        print(-1)
        continue
    shortest = dist1[end]
    
    q = deque([(0,end)])
    while q :
        curDist,curNode = q.popleft()
        for toNode,toDist in edge_reverse[curNode]:
            d = curDist + toDist
            if d + dist1[toNode] == shortest:
                if edge_check[toNode][curNode]:
                    edge_check[toNode][curNode] = False
                    q.append((d,toNode))
                
    
    ans = dijkstra(start,end,edge)
    print(ans[end] if ans != None else -1)
