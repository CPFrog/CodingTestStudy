# 17:28

import sys

input = sys.stdin.readline
n = int(input())

members = list(map(int, input().split()))

members.sort()

group = 0
need = members[0]-1
for x in members[1:]:
    if need == 0:
        group += 1
        need = x - 1
    else:
        need -= 1

#17:38


print(group)