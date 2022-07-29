'''
< set 함수 >

1) 교집합 : &
2) 합집합 : |
3) 차집합 : -

'''

# a : 집합 A의 원소의 개수, b : 집합 B의 원소의 개수
a, b = map(int, input().split())
arr = set(map(int, input().split())) # 집합 A (set 연산자 활용을 위해 사용)
brr = set(map(int, input().split())) # 집합 B

result = (arr - brr) | (brr - arr) # 대칭 차집합
print(len(result)) # 대칭 차집합의 원소의 개수 출력