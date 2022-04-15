# 문제를 못푼 이유
# 1. 선수 과목에 대한 시간 계산 불가
# 2. time[5]의 값이 이상하게 생신됨.

# 못 푼 원인에 대한 해결책
# 1. 인접한 노드(즉, 선수과목들)에 대해 현재보다 더 긴 선수과목 수강 소요 시간이 있다면 그 값으로 선수과목 소요 시간 갱신.
# 2. 리스트의 변수 값을 복사할 때 단순히 대입하면 의도치 않은 값의 변경이 일어날 수 있으므로 deepcopy()를 써야함. (cf. Python의 얕은복사, 깊은복사)

# 아래 코드는 위의 이슈들을 고민해본 후 책의 내용을 참고하며 수정한 코드.

from collections import deque
import copy
import sys

input = sys.stdin.readline
n = int(input())
enter_dim = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]  # 각 과목에 대한 선수 과목에 대한 정보 저장하기 위한 인접 리스트 선언
time = [0] * (n + 1)  # 각 강의를 듣는데 걸리는 시간을 0으로 초기화

# 과목별 정보 입력받음
for i in range(1, n + 1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    for x in line[1:-1]:
        enter_dim[i] += 1
        graph[x].append(i)

ans = copy.deepcopy(time)
q = deque()
for i in range(1, n + 1):
    if enter_dim[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for i in graph[cur]:
        ans[i] = max(ans[i], ans[cur] + time[i])
        enter_dim[i] -= 1
        if enter_dim[i] == 0:
            q.append(i)

for i in range(1, n + 1):
    print(ans[i])
