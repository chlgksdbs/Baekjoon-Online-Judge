data = input() # 식 입력
data_split = data.split('-') # 위에서 입력한 식을 '-'를 기준으로 나누어줌
result = 0 # 계산 결과 값을 담을 변수

for i in range(len(data_split)):
    data_split2 = data_split[i].split('+') # '-'를 기준으로 나누어진 리스트를 다시한번 '+'를 기준으로 나누어준다.
    if i == 0: # '-'가 나오기 전까지 부분은 더해준다.
        for j in range(len(data_split2)):
            result += int(data_split2[j])
    else: # '-'가 나온 이후부분은 모두 빼준다.
        for j in range(len(data_split2)):
            result -= int(data_split2[j])

print(result)


# 문자열.split() 함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어 주는 함수이다.
# eval() 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다. 그러나 여기서는 '00009'와 같은 케이스를 eval로 해결할 수 없으므로 사용하지 않는다.
