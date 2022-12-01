import sys

def cut_tree(arr, target, start, end):
    answer = 0 # 절단기에 설정할 수 있는 높이의 최댓값을 저장하는 변수
    while start <= end:
        mid = (start + end) // 2
        len_tree = 0 # mid 길이만큼 자르고 남은 나무의 길이

        for x in arr:
            if x > mid: # 자르려는 길이보다 나무의 길이가 클 경우 자른 나머지 값을 더하여 저장
                len_tree += x - mid
        
        if len_tree == target: # 자른 나무의 길이와 상근이가 필요한 나무의 길이가 같은 경우
            return mid
        elif len_tree > m: # 자른 나무의 길이가 상근이가 필요한 나무의 길이보다 큰 경우
            answer = mid
            start = mid + 1
        else: # 자른 나무의 길이보다 상근이가 필요한 나무의 길이가 큰 경우
            end = mid - 1
    
    return answer

# n : 나무의 수, m : 상근이가 집으로 가져가려고 하는 나무의 길이
n, m = map(int, input().split())
data = list(map(int, sys.stdin.readline().split())) # 나무의 높이
data.sort() # 이분탐색을 위한 리스트 오름차순 정렬

print(cut_tree(data, m, 0, data[-1]))