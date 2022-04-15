# 09:43

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (m + 1)

for i in range(1, n + 1):
    parent[i] = i


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


for _ in range(m):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union_parent(parent, a, b)
    if cmd == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')

# 09:58
# ---------- 개선할 부분 ----------
# 책에 있는 코드와 순서만 조금 다르거나 변수명만 다를뿐 같음.
