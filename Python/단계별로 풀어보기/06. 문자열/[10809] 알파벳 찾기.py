# -*- coding: utf-8 -*-

s = input() # 입력받은 문자열
for i in range(97, 123):
    if s.find(chr(i)) != -1:
        print(s.find(chr(i)), end=' ')
    else:
        print(-1, end=' ')

# 숫자를 아스키코드로 변환하는 방법은 chr()를 이용
# 반복문에서 출력을 줄바꿈이 아닌 띄어쓰기를 하고싶을 때는 출력문 끝에 end=' '를 이용
# 문자열에서 arg(인자)를 문자열내에서 찾아서 찾은 문자열의 가장 첫 부분의 오프셋을 반환하는 내장함수는 find(인자)를 이용
