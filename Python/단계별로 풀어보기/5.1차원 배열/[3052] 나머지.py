arr = []
count = 10
for i in range(10):
    x = int(input())
    nx = x % 42
    arr.append(nx)

for i in range(42):
    if arr.count(i) > 1:
        count = count - arr.count(i) + 1

print(count)
# list의 count() 함수를 사용하여 개수를 구함. 그러나 코드가 효율적으로 작성된 지는 잘 모르겠음.
