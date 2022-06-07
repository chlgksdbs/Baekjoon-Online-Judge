n = int(input()) # n : 단어의 개수
words = []
for _ in range(n): # 입력
    words.append(input())

words = list(set(words)) # 중복된 데이터 제거 (set 함수 사용 -> 중복을 허용하지 않음)
new_words = sorted(words) # (2) 사전순으로 정렬
new_words.sort(key = lambda x : len(x)) # (1) 길이가 짧은 순으로(오름차순) 정렬

for i in range(len(new_words)): # 출력
    print(new_words[i])