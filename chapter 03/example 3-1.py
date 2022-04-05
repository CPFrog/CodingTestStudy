change = 1260

coin = [500, 100, 50, 10]
ans = [] # 교재에는 전체 동전의 개수만 구하라고 했지만, 종류별로 구해보기 위해 리스트로 답 저장.
for value in coin:
    if (change // value) > 0:
        ans.append(change // value) # 파이썬에서는 정수끼리의 나눗셈도 실수로 표현되므로 // 연산자 써야함.
        change %= value
        # print(change) 디버깅용 출력문
    else:
        ans.append(0)

print(ans)
