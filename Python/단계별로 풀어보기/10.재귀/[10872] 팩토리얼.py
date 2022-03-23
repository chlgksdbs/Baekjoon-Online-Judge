sum = 1

def factorial(a): # 재귀함수 활용
    global sum
    if a == 0:
        return 1
    if a == 1:
        return sum
    else:
        sum = sum * a
        return factorial(a-1)

n = int(input()) # 입력

print(factorial(n))

# 4번째 line을 빼놓고 컴파일시에 'UnboundLocalError: local variable 'sum' referenced before assignment'와 같은 오류 발생
# 위와 같은 오류가 발생하는 이유는 함수 본문 내에서 할당 전에 일부 변수가 참조 될 때 발생함. 이 오류는 일반적으로 코드가 전역 변수에 액세스하려고 할 때 발생함.
