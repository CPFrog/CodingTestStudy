# 17:42

numbers = input()

zero_flag = False
ans = 0
for x in range(len(numbers)):
    cur = int(numbers[x])
    if cur == 0:
        ans += cur
    else:
        if ans == 0:
            ans += cur
        else:
            ans *= cur

print(ans)
#17:49