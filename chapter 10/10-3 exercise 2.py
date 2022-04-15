# 10:04
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
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    parent[i] = i

q = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    heapq.heappush(q, (cost, a, b))

ans = 0
max_cost = 0
while q:
    cost, x, y = heapq.heappop(q)
    if not is_cycle(parent, x, y):
        union_parent(parent, x, y)
        ans += cost
        if max_cost < cost:
            max_cost = cost

print(ans - max_cost)

# 10:24

# ---------- 개선할 부분 ----------
# 이 문제는 실제 백준에 있는 문제. (1647번)
# 제출했더니 시간 초과 나왔음.
# 굳이 heapq 이용해서 풀어야만 했을까?
