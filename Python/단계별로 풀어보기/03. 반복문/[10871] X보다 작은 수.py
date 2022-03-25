a = input().split()
b = input().split()
n = int(a[0])
x = int(a[1])

list = [] # 빈 리스트 생성

for i in range(n):
    if int(b[i]) < x:
        list.append(b[i])

print(" ".join(str(i) for i in list))

# join으로 list를 한 줄로 출력함
