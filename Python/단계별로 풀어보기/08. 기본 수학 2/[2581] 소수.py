m = int(input())
n = int(input()) # m <= n
psum = 0 # 소수의 합을 계산할 변수
pmin = 0 # 소수의 최솟값을 계산할 변수

for i in range(n, m - 1, -1): # m이상 n이하, 반복문을 거꾸로 돌려서 pmin에 최솟값이 들어가게함
    pcheck = True # 소수임을 체크하는 변수
    if i == 1: # m = 1부터 시작할 때,
        psum += 0
    else:
        for j in range(2, i): # i가 소수임을 판별
            if i % j == 0:
                pcheck = False
                break
        if pcheck == True:
            psum += i
            pmin = i

if psum == 0:
    print(-1)
else:
    print(psum)
    print(pmin)
