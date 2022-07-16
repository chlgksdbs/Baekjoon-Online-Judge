n = int(input()) # n! 에서의 n의 크기

n_factorial = 1 # n!의 결과 값을 저장
zero_count = 0 # n!에서 0의 개수
zero_start = 0 # 0의 count가 시작한 시점
for i in range(n, 0, -1):
  n_factorial *= i

n_factorial = str(n_factorial) # int형의 변수를 str형으로 형 변환

for i in range(len(n_factorial) - 1, -1, -1): # 뒤에서 부터 확인
  if n_factorial[i] == '0':
    zero_count += 1
    zero_start = 1 # 플래그 값 변경
    continue
  
  if zero_start == 1 and n_factorial[i] == '0': # 플래그 값이 참이면서, 해당 인덱스의 값이 0인 경우
      zero_count += 1
  elif zero_start == 1: # 플래그 값은 참이지만, 해당 인덱스의 값이 0이 아닌 경우
      break

print(zero_count)
