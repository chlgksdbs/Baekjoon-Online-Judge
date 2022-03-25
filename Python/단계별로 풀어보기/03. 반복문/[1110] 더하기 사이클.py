n = int(input())
vn = n # while문에서 사용될 입력 값 n
cycle = 1

while True:
    x = vn // 10 # n의 10의 자리 수
    y = vn % 10 # n의 1의 자리 수
    sum = x + y
    newNumber = y * 10 + (sum % 10)

    if n == newNumber:
        break
    else:
        cycle += 1

    vn = newNumber

print(cycle)
