from collections import deque
import sys

class Node():
    def __init__(self):
        self.adjacent = []
        self.visited = False


input = sys.stdin.readline
n, m, start = map(int,input().split())
vertex = [list(map(int,input().split())) for _ in range(m)]
node_dict = dict(zip(range(1,n+1), [Node() for i in range(n)]))

for v in vertex:
    for idx, node in enumerate(v):
        node_dict[node].adjacent.append(v[1-idx])

dfs, bfs = [start], [start]

curr_node = node_dict[start]
stack = sorted(curr_node.adjacent, reverse=True)
curr_node.visited=True

while stack:
    curr = stack.pop()
    curr_node = node_dict[curr]

    if not curr_node.visited:
        dfs.append(curr)
        for neighbor in sorted(curr_node.adjacent, reverse=True):
            if not node_dict[neighbor].visited:
                stack.append(neighbor)
        curr_node.visited = True

print(' '.join([str(i) for i in dfs]))


for _, node in node_dict.items():
    node.visited = False


curr_node = node_dict[start]
queue = deque(sorted(curr_node.adjacent))
curr_node.visited = True

while queue:
    curr = queue.popleft()
    curr_node = node_dict[curr]

    if not curr_node.visited:
        bfs.append(curr)
        for neighbor in sorted(curr_node.adjacent):
            if not node_dict[neighbor].visited:
                queue.append(neighbor)
        curr_node.visited = True


print(' '.join([str(i) for i in bfs]))