n = int(input()) # n : 정수의 개수
nList = list(map(int, input().split())) # nList : n개의 정수를 담은 리스트
v = int(input()) # v : 찾으려고 하는 정수
vCount = 0 # vCount : v의 개수를 저장하는 변수

for x in nList:
    if x == v:
        vCount += 1
    
print(vCount)
