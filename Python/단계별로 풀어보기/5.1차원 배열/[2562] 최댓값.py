arr = []
for i in range(0, 9):
    arr.append(int(input()))
arr_max = arr[0]
arr_index = 0

for i in range(1, 9):
    if arr_max < arr[i]:
        arr_max = arr[i]
        arr_index = i
print(arr_max)
print(arr_index + 1)

# 파이썬에서 배열을 한 줄로 입력받을 때 arr[i] = int(input())과 같은 형태가 아니라, append를 활용하여 입력받는다.
