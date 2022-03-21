n = int(input()) # n kilogram input
# 관계식 : 5a + 3b = N 으로 가정, 이 때 a의 크기가 클수록 최솟값임
a = n // 5 # 위 관계식에 따라 a값 설정
ans = False # 반복문에서 정답이 나왔는지 유무확인
for i in range(a, -1, -1): # a의 값을 a -> 0까지 감소시키면서 b값을 찾음
    if (n - 5*i) % 3 == 0:
        b = (n - 5*i) // 3 # b값 설정
        print(i + b)
        ans = True
        break
if ans == False:
    print(-1)
