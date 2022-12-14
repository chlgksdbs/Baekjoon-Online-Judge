import sys
from bisect import bisect_left, bisect_right

def count_by_range(a, value): # 값이 value 인 데이터의 개수를 반환하는 함수
    right_index = bisect_right(a, value)
    left_index = bisect_left(a, value)
    return right_index - left_index

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return count_by_range(array, array[mid])
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0

n = int(input()) # n : 상근이가 가지고 있는 숫자 카드의 개수
data = list(map(int, sys.stdin.readline().split()))
data.sort() # 이분 탐색을 위한 오름차순 정렬

m = int(input()) # m : 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 정수의 개수
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    result = binary_search(data, target, 0, n - 1)
    print(result, end = ' ')

print()
