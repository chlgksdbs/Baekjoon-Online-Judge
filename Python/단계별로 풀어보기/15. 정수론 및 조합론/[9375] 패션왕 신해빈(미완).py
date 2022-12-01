t = int(input()) # t : 테스트 케이스의 개수
for _ in range(t):
    n = int(input()) # n : 해빈이가 가진 의상의 수
    clothes = []
    for _ in range(n):
        # c_name : 의상의 이름, c_type : 의상의 종류
        c_name, c_type = input().split()
        clothes.append([c_name, c_type])
    
    count = count(clothes) # 알몸이 아닌 상태로 의상을 입을 수 있는 경우의 수 (1개 입은 상태의 수로 초기화)

    for x, y in clothes:
        