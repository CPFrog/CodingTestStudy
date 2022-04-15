# 기존 코드와 달라진점
# 1. heap queue 사용하는거 배제
# 2. 대신 도로에 대한 정보를 저장하고 비용이 낮은 순서대로 정렬한 뒤, 하나씩 검색하며 min spanning tree 생성.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def is_cycle(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return True
    else:
        return False


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

ans = 0
max_cost = 0
for cost, x, y in edges:
    if not is_cycle(parent, x, y):
        union_parent(parent, x, y)
        ans += cost
        if max_cost < cost:
            max_cost = cost

print(ans - max_cost)
