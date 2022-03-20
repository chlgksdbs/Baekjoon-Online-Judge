n = int(input())
i = 0 # while 반복문 안에 사용될 변수, 최소 개수의 방을 count하는 변수로 사용
bul = 1 # 벌집의 방

while True:
    if n <= bul:
        break
    else:
        i += 1
        bul += (6 * i)

print(i + 1) # 1을 포함하기 때문에 더해줌
