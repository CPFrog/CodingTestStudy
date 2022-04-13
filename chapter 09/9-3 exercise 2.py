# 실전문제 2 - 전보.
# 최저의 비용으로 최대한 많은 도시 돌면서 긴급상황 알리기.

# 13:23
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) # 도시의 개수 n, 통로의 개수 m, 시작점 c

graph = [[] for _ in range(n + 1)]  # 그래프의 정보를 인접 리스트로 만들기 위한 리스트 변수 생성.
distance = [INF] * (n + 1)  # 각 도시의 거리 정보가 저장되는 리스트

for _ in range(m):
    x, y, z = map(int, input().split()) # 경로의 시작점 x, 끝점 y, 비용 z (단방향 경로임)
    graph[x].append((y, z))

# 다익스트라 시작
q = []
heapq.heappush(q, (c, 0))

while q:
    cur, cost = heapq.heappop(q)

    for next, bill in graph[cur]:
        if distance[next] > cost + bill:
            distance[next] = cost + bill
            heapq.heappush(q, (next, distance[next]))

# 다익스트라 끝

cnt = 0
cost = 0
for i in range(n + 1):
    if distance[i] == INF:
        distance[i] = -1
    else:
        cnt += 1
        cost = max(cost, distance[i])

print(cnt, cost)

# 13:41

# 테스트케이스: 3 2 1 / 1 2 4 / 1 3 2 || 정답: 2 4

# ---------- 개선할 부분 ----------
# Line 22: 처음 시작점의 거리를 0으로 초기화 하는 코드 빠짐. (만약 포함시킬 경우 Line 37의 cnt 값 1개 빼줘야 함. 0도 INF가 아니라 count되므로)
# Line 26: if distance[cur]<cost: continue 라는 코드 써서 불필요한 반복문 수행 줄일 수 있음.
# Line 38, 39: 불필요한 코드. (INF가 아닐 경우의 조건 걸어서 cnt 값 1 증가시키고 최대 값만 포함시키면 됨.)
