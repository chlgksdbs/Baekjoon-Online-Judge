from bisect import bisect_left, bisect_right

# 값이 [Value, Value]인 데이터의 개수를 반환하는 함수
def countCard(data, Value):
    leftIdx = bisect_left(data, Value)
    rightIdx = bisect_right(data, Value)

    return rightIdx - leftIdx

n = int(input()) # n : 상근이가 가지고 있는 숫자 카드의 개수
numCard = list(map(int, input().split()))
numCard.sort() # 이분 탐색을 위한 오름차순 정렬

m = int(input()) # m : 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 정수
checkCard = list(map(int, input().split()))

for x in checkCard:
    if countCard(numCard, x): # 함수를 통해 return된 값이 0이 아닌 경우
        print(countCard(numCard, x), end = ' ')
    else:
        print(0, end = ' ')
