n = int(input()) # n개의 수
a = input().split()
arr = []
count = 0 # 소수의 개수를 count하는 변수
for i in range(n):
    arr.append(int(a[i]))
for j in range(len(arr)):
    k = 0
    for k in range(2, arr[j]): # 각각 수마다 소수인지 체크
        if arr[j] % k == 0:
            break
    if arr[j] == 1: # arr[j]가 1이라면,
        count += 0
    elif arr[j] == 2: # arr[j]가 2라면,
        count += 1
    elif k == arr[j] - 1: # arr[j]가 소수라면,
        count += 1
print(count)
