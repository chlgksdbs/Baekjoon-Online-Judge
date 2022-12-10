while True:
    s = list(input()) # s : 입력받은 문자열

    if s[0] == '.': # 입력의 종료조건
        break
    
    stack = [] # stack : 소괄호와 대괄호를 담는 스택

    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(': # stack에 원소가 한 개 이상 존재하고, top의 원소가 '('인 경우
                stack.pop()
            else:
                print("no")
                break
        elif x == '[':
            stack.append(x)
        elif x == ']':
            if stack and stack[-1] == '[': # stack에 원소가 한 개 이상 존재하고, top의 원소가 '['인 경우
                stack.pop()
            else:
                print("no")
                break
    else: # for ~ else 문
        if stack: # 스택의 원소가 남아 있는 경우, 짝이 지어지지 않았으므로 "no"를 출력
            print("no")
        else:
            print("yes")
