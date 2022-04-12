# 플로이드 알고리즘: 모든 노드에서 모든 노드로 이동하는 가장 짧은 경로의 길이 구하는 알고리즘.
# 시간복잡도-> O(N^3) (cf. 개선된 다익스트라: O(ElogV)
# 굳이 배워야 할 필요 있나..?

# 구현 시작

import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

# 그래프를 2차원 리스트 형태로 만들고, 모든 값을 INF로 초기화
graph = [[INF] * (n + 1)] * (n + 1)

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    sp, ep, dist = map(int, input().split())
    graph[sp][ep] = dist

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

for start in range(1, n + 1):
    for end in range(1, n + 1):
        # 도달할 수 없는 경우 무한대(INFINITY)라는 문구 출력
        if graph[start][end] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[start][end],end=' ')
    print()
