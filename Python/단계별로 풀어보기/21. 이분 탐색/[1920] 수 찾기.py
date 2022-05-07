def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target: # 찾은 경우 1을 반환
            return 1
        elif arr[mid] > target: # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            end = mid - 1
        else: # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            start = mid + 1
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort() # 이분 탐색을 위한 오름차순 정렬

m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    if binary_search(a, b[i], 0, n - 1): # 해당 값이 존재한다면 1을 출력
        print(1)
    else: # 해당 값이 존재하지 않는다면 0을 출력
        print(0)
