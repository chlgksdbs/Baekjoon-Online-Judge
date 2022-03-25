n = input().split()
a = int(n[0]) # A미터만큼 올라감
b = int(n[1]) # B미터만큼 내려감
v = int(n[2]) # 나무 막대의 높이 V미터

temp = (v - b) // (a - b) # (n-1)(a-b) + a >= v 등식에서부터 나온 식

if (v - b) % (a - b) == 0:
    print(temp)
else:
    print(temp + 1)
