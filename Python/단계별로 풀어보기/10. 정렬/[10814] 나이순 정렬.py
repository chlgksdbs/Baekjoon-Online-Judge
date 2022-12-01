n = int(input()) # n : 온라인 저지 회원의 수
data = []
for _ in range(n): # 입력
	age, name = input().split()
	data.append([int(age), name])
data.sort(key = lambda x : x[0])

for i in range(n): # 출력
	print(data[i][0], data[i][1])
