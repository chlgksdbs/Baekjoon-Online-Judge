import sys

n = int(input()) # n : 명령의 개수
stack_list = [] # 스택 리스트

for _ in range(n):
    data = list(map(str, sys.stdin.readline().split())) # 명령어 입력
    if len(data) == 2: # push 명령어
        stack_list.append(data[1])
    else:
        if data[0] == "pop": # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
            if stack_list:
                print(stack_list.pop())
            else: # 스택에 들어있는 정수가 없는 경우
                print(-1)
        
        elif data[0] == "size": # 스택에 들어있는 정수의 개수 출력
            print(len(stack_list))

        elif data[0] == "empty": # 스택이 비어있으면 1, 아니면 0을 출력
            if stack_list:
                print(0)
            else:
                print(1)
        
        elif data[0] == "top": # 스택의 가장 위에 있는 정수를 출력
            if stack_list:
                print(stack_list[-1])
            else:
                print(-1) # 스택에 들어있는 정수가 없는 경우
