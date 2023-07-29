from collections import deque
import sys

class Node():
    def __init__(self):
        self.visited=False
        self.adjacent=[]


input = sys.stdin.readline
v,e,r = map(int,input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

v_dict = dict(zip(range(1,v+1),[Node() for _ in range(v)]))

for edge in edges:
    for idx, vertex in enumerate(edge):
        v_dict[vertex].adjacent.append(edge[1-idx])
        
start_node = v_dict[r]
start_node.visited = True
queue = deque(sorted(start_node.adjacent))
route = [r]

while queue:
    curr = queue.popleft()
    curr_node = v_dict[curr]
    
    if not curr_node.visited:
        route.append(curr)
        curr_node.visited = True
        
        for neighbor in sorted(curr_node.adjacent):
            if not v_dict[neighbor].visited:
                queue.append(neighbor)

order_dict = dict(zip(range(1,v+1),[0]*v))

for idx, vertex in enumerate(route):
    order_dict[vertex] = idx+1

for i in range(1,v+1):
    print(order_dict[i])
