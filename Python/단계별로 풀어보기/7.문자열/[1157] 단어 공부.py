# -*- coding: utf-8 -*-

s = input()
s = s.upper() # 문자열을 모두 대문자로 변경
count = []
index = -1

for i in range(65, 91): # chr(65) = 'A', chr(90) = 'Z'
    count.append(s.count(chr(i))) # count 리스트에 각 알파벳 별로 count수를 추가

maxc = max(count) # count 리스트의 최댓값
cnt = 0 # count 리스트의 최댓값 갯수를 저장하는 변수
alpha = -1 # count 리스트의 최댓값을 가지는 문자를 저장하는 변수

for j in range(len(count)):
    if maxc == count[j]:
        cnt += 1
        alpha = j


if cnt == 1:
    print(chr(65 + alpha))
else:
    print('?')


# 문자열 내장함수 중, upper()을 사용하면 문자열이 모두 대문자로 바뀌고 lower()를 사용하면 문자열이 모두 소문자로 변경됨
# 문자열 내장함수 중, chr()를 사용하면 숫자를 아스키코드로 변경하고 ord()를 사용하면 아스키코드를 숫자로 변경함
