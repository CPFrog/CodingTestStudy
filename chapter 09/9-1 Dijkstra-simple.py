import sys

input = sys.stdin.readline  # 파이썬 내장 함수인 input을 더 빠르게 동작하는 sys.stdin.readline으로 대체
INF = int(1e9)  # 일반적인 코딩테스트 문제에서는 10억 이상의 값을 안줌(C/C++ 때문에). 따라서 충분히 큰 수인 10억을 무한대 숫자로 취급

n, m = map(int, input().split())
start = int(input())  # 시작 노드번호
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cost = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 인접 리스트 방식으로 그래프 사용


# 방문하지 않은 노드 중 가장 비용이 적은(최단거리의) 노드 번호 반환
def get_next_dest():
    min_val = INF
    index = 0
    for i in range(1, n + 1):
        if cost[i] < min_val and not visited[i]:
            min_val = cost[i]
            index = i
    return index


def dijkstra(start):
    cost[start] = 0
    visited[start] = True
    for j in graph[start]:
        cost[j[0]] = j[1]
    for i in range(n - 1):
        next_node = get_next_dest()
        visited[next_node] = True
        for j in graph[next_node]:
            tmp = cost[next_node] + j[1]
            if tmp < cost[j[0]]:
                cost[j[0]] = tmp


dijkstra(start)

for i in range(1, n + 1):
    if cost[i] == INF:
        print("INFINITY")
    else:
        print(cost[i])

# 최단거리가 가장 짧은 노드를 매번 선형탐색 및 연결된 노드를 매번 확인.
# 노드가 10000개가 넘어가면 시간복잡도가 O(V^2)인 이 코드로는 해결 불가.
