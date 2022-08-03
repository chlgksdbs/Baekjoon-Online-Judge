'''
모든 약수에 대하여, 가운데 약수를 기준으로 해서 각 등식이 대칭적인 형태를 보인다.
따라서 특정한 자연수 X가 소수인지 확인하기 위하여 바로 가운데 약수까지만 '나누어떨어지는지' 확인하면 된다.
다시 말해 제곱근까지만 (가운데 약수까지만) 확인하면 된다는 점을 기억하자.
'''

import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어지는 경우
        if x % i == 0:
            return False # 소수가 아님
    
    return True # 소수임

m, n = map(int, input().split())
for x in range(m, n + 1):
    # x가 1이 아니고, 소수 판별 함수의 값이 True인 경우
    if x != 1 and is_prime_number(x):
        print(x)