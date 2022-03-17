# -*- coding: utf-8 -*-

t = int(input()) # Test case
for i in range(t):
    x = input().split()
    r = int(x[0]) # 반복횟수
    s = x[1] # 입력받은 문자열
    s = str(s) # s를 string형으로 형변환
    for j in range(len(s)):
        for k in range(r):
            print(s[j], end='')
    print() # 입력문과 출력문 사이 줄바꿈을 위해 삽입
