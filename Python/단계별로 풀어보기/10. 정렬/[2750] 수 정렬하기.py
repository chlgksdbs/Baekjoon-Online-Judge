n = int(input()) # N : 수의 개수
arr = [] # N개의 수를 담을 배열

for i in range(n):
    x = int(input())
    arr.append(x)

for i in range(n):
    for j in range(i, n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            # 버블 정렬

for i in range(n):
    print(arr[i])
