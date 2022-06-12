n, k = map(int, input().split())
cnt = k # 반복문 반복 횟수
n_molecule = 1 # 분자
n_denominator = 1 # 분모

if 0 <= k and k <= n: # 이항 계수 조건 (1)
    for _ in range(cnt): # 분자 계산
        n_molecule *= n
        n -= 1
    for _ in range(cnt): # 분모 계산
        n_denominator *= k
        k -= 1
    print(n_molecule // n_denominator)
    
else:
    print(0) # 이항 계수 조건 (2)