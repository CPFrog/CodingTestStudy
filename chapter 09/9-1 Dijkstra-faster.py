# 우선순위 큐(힙을 이용한 자료구조)를 이용해 속도 개선
# 구현은 복잡하지만 매우 빠른 방법
# 파이썬에서도 C++의 STL(queue 라이브러리)에서 제공하는 priority_queue처럼 PriorityQueue가 있음.
# 하지만, heapq가 훨씬 더 빠르게 동작하기 때문에 heapq를 사용

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
cost = [INF] * (n + 1)

for _ in range(m):
    start_point, end_point, distance = map(int, input().split())
    graph[start_point].append((end_point, distance))  # sp에서 ep로 가는 비용이 distance만큼 든다.


def dijkstra(begin):
    q = []
    heapq.heappush(q, (0, start))  # 최초 시작점으로의 거리는 0으로 취급하여 큐에 넣음
    cost[begin] = 0

    while q:
        dist, next_node = heapq.heappop(q)
        if cost[next_node] < dist:
            continue
        for i in graph[next_node]:
            tmp = dist + i[1]  # 현재 노드를 거쳐서 다음 노드로 이동하는 거리가 더 짧은 경우
            if tmp < cost[i[0]]:
                cost[i[0]] = tmp
                heapq.heappush(q, (tmp, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if cost[i] == INF:
        print("INFINITY")
    else:
        print(cost[i])
