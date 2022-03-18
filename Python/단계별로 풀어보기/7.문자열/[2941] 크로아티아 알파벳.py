s = input() # 입력으로 주어진 단어
cnt = 0 # 알파벳 갯수를 세는 변수

s = s.replace('c=', 'a')
s = s.replace('c-', 'a')
s = s.replace('dz=', 'a')
s = s.replace('d-', 'a')
s = s.replace('lj', 'a')
s = s.replace('nj', 'a')
s = s.replace('s=', 'a')
s = s.replace('z=', 'a')

print(len(s))

# 파이썬의 문자열 내장함수 중에 replace()를 사용하여 크로아티아의 변경된 알파벳을 전부 기본 알파벳인 a로 변경하여 문자열의 길이를 구했다.
# 파이썬의 문자열 내장함수에는 편하게 코딩할 수 있는 함수가 정말 많다.
