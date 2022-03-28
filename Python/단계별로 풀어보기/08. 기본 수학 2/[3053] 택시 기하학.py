import math

r = int(input()) # R : 반지름
pi = math.pi # pi의 크기

print("{:.6f}".format(pi * (r ** 2))) # 유클리드 기하학
print("{:.6f}".format(2 * r * r)) # 택시 기하학
