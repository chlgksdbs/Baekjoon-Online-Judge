def recursion(s, start, end):
    if start >= end:
        return 1, start + 1
    elif s[start] != s[end]:
        return 0, start + 1
    else:
        return recursion(s, start + 1, end - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

T = int(input())

for _ in range(T):
    s = list(input()) # s : 알파벳 대문자로 구성된 문자열

    # returnValue : isPalindrome 함수의 반환 값
    # recursionCount : recursion 함수의 호출 횟수
    returnValue, recursionCount = isPalindrome(s)

    print(returnValue, recursionCount)
