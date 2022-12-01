n = int(input()) # n : 테스트 데이터의 개수

for _ in range(n):
    data = list(input()) # 괄호 문자열 입력
    left_cnt = 0 # '(' 문자의 개수를 세는 변수
    right_cnt = 0 # ')' 문자의 개수를 세는 변수
    answer = -1

    while True:
        if len(data) == 0: # 리스트에 원소가 없는 경우 반복문 탈출
            answer = 1
            break
        
        if data.pop() == ')':
            right_cnt += 1
        else:
            left_cnt += 1
        
        if left_cnt > right_cnt or right_cnt - left_cnt > 1:
            answer = 0
            break

    if answer == 0:
        print("NO")
    else:
        print("YES")
