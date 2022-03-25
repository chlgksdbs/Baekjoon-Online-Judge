# arr = map(int, input().split())
# arr = list(arr) # map class -> list
def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

# print(solve(arr))
# 문제에서 요구하는 정답 부분은 
