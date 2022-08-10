total_amount = int(input()) # total_amount : 영수증에 적힌 총 금액
n = int(input()) # n : 구매한 물건의 종류의 수

check_amount = 0 # 물건의 가격과 개수로 계산한 총 금액

for _ in range(n):
    # a : 물건의 가격, b : 개수
    a, b = map(int, input().split())
    check_amount += (a * b)

if total_amount == check_amount:
    print("Yes")
else:
    print("No")
