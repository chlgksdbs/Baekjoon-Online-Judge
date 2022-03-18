n = input().split()
a = n[0]
b = n[1]
r_a = '' # 새로운 A
r_b = '' # 새로운 B

for i in a:
    r_a = i + r_a # A 문자열 순서 뒤집기
for j in b:
    r_b = j + r_b # B 문자열 순서 뒤집기
r_a = int(r_a)
r_b = int(r_b)
if r_a > r_b:
    print(r_a)
else:
    print(r_b)

# for문을 이용해 문자열 뒤집는 알고리즘을 배웠다.
# 위 for문에서 우변의 순서가 바뀌면 뒤집기가 안된다는 것을 명심하자.
