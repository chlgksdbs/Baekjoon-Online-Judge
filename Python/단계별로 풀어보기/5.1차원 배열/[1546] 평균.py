# -*- coding: utf-8 -*-
n = int(input())
score = map(int, input().split()) # 세준이의 n개 과목에 대한 현재 점수
score = list(score)
sum = 0 # 총 점수
m = score[0] # 최고점을 구하기 위한 변수 선언
for i in range(1, n):
    if m < score[i]:
        m = score[i]
for i in range(n):
    score[i] = score[i] / m * 100
    sum += score[i]
print(sum / len(score))
# python에서 띄어쓰기로 정수형을 입력받기 위해서는 map(int, input().split())을 활용해야함
# python에서 map()으로 입력받으면 map class이기 때문에, []를 사용하여 인덱스를 통해 접근하려면 []이 사용가능한 list같은 자료형으로 캐스팅해야함
# list의 길이를 구하는 함수는 list.len() 이 아니라 len(list)임
