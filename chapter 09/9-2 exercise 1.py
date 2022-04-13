# 실전문제 1 - 미래 도시
# 양방향 경로에 대해 하나의 경유지를 거쳐 최종 목적지로 가장 빨리 가는 최소의 비용 구하기
# 각 경로의 이동 비용은 1.

# 9:08

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 도시의 개수 n, 경로의 개수 m

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())  # 경로의 양 끝
    graph[start][end] = 1  # 양방향 경로이므로 각각의 인접리스트에 서로를 추가함.
    graph[end][start] = 1

x, k = map(int, input().split())  # 목적지 x, 경유지 k

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1) # 경유지를 거쳐 목적지를 가는 경로가 없는 경우 -1 출력
else:
    print(graph[1][k] + graph[k][x]) # 있을 경우 그 경로의 비용 출력

# 9:39
# -> graph의 선언을 [[INF]*(n+1)]*(n+1)로 했다가 그 세로열 전체가 바껴버리는 뭐같은 경우 발생.

# ---------- 개선할 부분 ----------
# Line 26부터 >> 굳이 생으로 graph를 갖다 쓸 필요가 있나?
# cost=graph[1][k]+graph[k][x]로 하고 cost만 쓰면 if문도 그렇고 출력문도 깔끔해질텐데.

# 나를 골탕먹였던 세로열 전체 바뀌는 문제 해결하면서 더 빠른 2차원 배열 선언하는 방법:
# [[INF]*(n+1) for _ in range(n+1)]
# 아마 각 행을 생성할 때 * 식으로 되어있어서 복사처리가 되지 않았나 싶기도 하고..
# 반복문으로 생성하게 되면서 각각의 객체로 처리되는거 같다.
