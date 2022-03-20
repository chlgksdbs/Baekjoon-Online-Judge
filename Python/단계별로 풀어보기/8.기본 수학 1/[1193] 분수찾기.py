x = int(input()) # x번째 분수 입력
b = 1 # 분자 + 분모의 크기를 알 수 있게하는 변수 (끝부분)
cnt = 1 # 반복문의 횟수를 count하는 변수

while True:
    if b >= x:
        break
    else:
        cnt += 1
        b += cnt

a = b - cnt + 1 # 분자 + 분모의 크기를 알 수 있게하는 변수 (시작부분)

if cnt % 2 == 0: # 경우의 수가 짝수일 때,
    m = 1
    n = cnt # 원래 식은 (cnt + 1) - 1 이여야함, (cnt + 1)은 분모 + 분자의 합
    for i in range(a, b + 1):
        if x == i:
            print(m, "/", n, sep='')
            break
        else:
            m += 1
            n -= 1
else: # 경우의 수가 홀수일 때,
    m = cnt
    n = 1
    for j in range(a, b + 1):
        if x == j:
            print(m, "/", n, sep='')
            break
        else:
            m -= 1
            n += 1
