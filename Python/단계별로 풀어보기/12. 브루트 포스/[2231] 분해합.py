n = int(input()) # 분해합 n 입력
result = 0 # 생성자를 대입할 변수

for i in range(1, n): # 생성자 찾기
    for j in range(1, 8): # i의 자릿수 구하기 (10 ~ 10,000,000) 범위
        if i // (10 ** j) == 0:
            i_size = j - 1
            break
    
    sum_i = i # sum에 i값을 대입, sum은 각 자리수의 합을 포함하여 분해합을 계산할 변수
    x = i # x에 i값을 대입, x는 i값을 10의 거듭제곱으로 나누고 나머지 값을 저장할 변수
    for k in range(i_size, -1, -1): # (i_size ~ 0)
        sum_i += x // (10 ** k) # x의 각 자리수를 sum_i에 더함
        x %= (10 ** k) # x값을 감소
    if sum_i == n:
        result = i 
        break

print(result)
