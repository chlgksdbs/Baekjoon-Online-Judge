n = int(input()) # n : 테스트 데이터의 개수

for _ in range(n):
    data = list(input()) # 괄호 문자열 입력
    left_cnt = 0 # '(' 문자의 개수를 세는 변수
    right_cnt = 0 # ')' 문자의 개수를 세는 변수
    answer = 0

    while True:
        if not data: # 리스트에 원소가 없는 경우 반복문 탈출
            answer = 1
            break

        x = data.pop(0)
        
        if x == ')':
            right_cnt += 1
        elif x == '(':
            left_cnt += 1
        
        if left_cnt < right_cnt:
            break

    if answer == 0 or left_cnt != right_cnt:
        print("NO")
    else:
        print("YES")

"""
* 베스트 코드 *

T = int(input())

for _ in range(T):
    stack = []
    a = input()

    for x in a:
        if x == '(': # (1) '('가 들어오면 stack에 넣어준다.
            stack.append(x)
        elif x == ')': # (2) ')'가 들어오면 stack을 검사해, 비어있다면 NO를 출력한 뒤 break하고 만약 비어있지 않다면 pop을 해준다.
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: # for-else 문 사용 시, for문에서 중간에 break가 난적이 없고 끝까지 수행 되었을 때 else문 실행
        if not stack: # stack이 비어있는 경우 괄호의 짝이 모두 맞은 경우
            print("YES")
        else: # stack이 비어있지 않다면 괄호의 짝이 맞지 않은 경우
            print("NO")

"""
