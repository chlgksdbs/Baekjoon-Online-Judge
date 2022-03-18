from string import ascii_lowercase # 알파벳 소문자들

n = int(input()) # 단어의 개수
cnt = 0 # 그룹 단어의 갯수를 세는 변수

for i in range(n):
    s = input() # 단어
    j = 0 # s 문자열의 인덱스를 위한 변수
    alpha_list = list(ascii_lowercase)  # 알파벳 소문자들의 리스트
    while j < len(s):
        if s[j] in alpha_list:
            alpha = s[j] # s[j]의 문자를 변수에 저장
            while j < len(s):
                if s[j] != alpha:
                    break
                j += 1
            alpha_list.remove(alpha) # 알파벳 소문자들의 리스트에서 해당 알파벳을 제거
        else:
            break
    if j == len(s):
        cnt += 1
print(cnt)

# 리스트에서 특정 원소를 찾기위해서는 if '원소' in 리스트: 와 같은 문법을 사용한다.
# 알파벳 소문자들의 리스트를 만들기 위해서 string의 ascii_lowercase를 import 시켜서 사용한다.
# 리스트에서 특정 원소를 제거하기 위해서는 remove(원소)와 같은 문법을 사용한다.
# 16번째 line에 있는 명령문이 if문 보다 앞에 있을 시에, 인덱스 오류가 발생한다.
