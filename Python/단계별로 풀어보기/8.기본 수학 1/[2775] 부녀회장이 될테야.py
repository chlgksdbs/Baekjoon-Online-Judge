t = int(input()) # test case
for i in range(t):
    k = int(input()) # k층
    n = int(input()) # n호
    arr = [] # 각 층 별 인원 수를 담을 리스트
    for j in range(0, n): # 리스트 초기화
        arr.append(j + 1) # 0층의 인원 수를 담은 리스트
    for m in range(1, k): # 1 ~ (k-1)층 계산 반복
        v = 0  # 계산을 도와 줄 변수
        for n in range(1, n + 1): # 1 ~ n호 반복
            v += arr[n-1]
            arr[n-1] = v # 다음 층으로 리스트 요소를 변경
    print(sum(arr))
