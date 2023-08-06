def pre_order(o):
    if o != '.':
        print(o, end='')
        pre_order(tree[o][0])
        pre_order(tree[o][1])

def in_order(o):
    if o != '.':
        in_order(tree[o][0])
        print(o, end='')
        in_order(tree[o][1])

def post_order(o):
    if o != '.':
        post_order(tree[o][0])
        post_order(tree[o][1])
        print(o, end='')

n = int(input())
tree = {}

for _ in range(n):
    o,l,r = input().split()
    tree[o] = [l,r]

pre_order('A')
print()
in_order('A')
print()
post_order('A')
