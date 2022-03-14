n = int(input())
arr = list(map(int, input().split()))
arr_max = arr[0]
arr_min = arr[0]
for i in range(n):
    if arr_max < arr[i]:
        arr_max = arr[i]
    if arr_min > arr[i]:
        arr_min = arr[i]
print(arr_min, arr_max)

# 파이썬에서는 n만큼 크기의 입력을 정해두고 받지않고, 입력을 받은 뒤 반복문에서 n만큼 반복하여 마치 n만큼 입력받은 것 같은 효과를 낸다.
