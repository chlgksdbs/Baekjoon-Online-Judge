n = int(input())

numList = [] # numList : 만들고자 하는 수열
strList = [] # strList : '+', '-' 문자를 담는 리스트
for _ in range(n):
    num = int(input())
    numList.append(num)

stack = [] # stack : 1 ~ n까지의 수를 넣었다가 빼는 스택
idx = 0 # idx : numList의 원소를 가리키는 인덱스

for x in range(1, n + 1):
    # push 연산
    stack.append(x)
    strList.append('+')

    if stack and x == numList[idx]: # pop 연산
        stack.pop()
        idx += 1
        strList.append('-')
        
        while True:
            if stack and stack[-1] == numList[idx]:
                stack.pop()
                idx += 1
                strList.append('-')
            else:
                break

if stack: # stack에 원소가 남아있는 경우
    print("NO")
else:
    for x in strList:
        print(x)
