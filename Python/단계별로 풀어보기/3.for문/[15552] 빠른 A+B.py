import sys

t = int(input()) # Test case
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아짐
# map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수
