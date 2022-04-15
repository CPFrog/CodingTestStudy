# 13:02

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
enter = [0] * (n + 1)
next = [[] for _ in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if j == 0:
            time[i] = line[j]
        else:
            if line[j] != -1:
                next[line[j]].append(i)
                enter[i] += 1

q = deque()
for i in range(1, n + 1):
    if enter[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur)
    for i in next[cur]:
        enter[i] -= 1
        time[i] += time[cur]
        if enter[i] == 0:
            q.append(i)

print(time)

# 13:38 give up
