n = int(input())
cnt = 0 # 한수의 개수를 세기 위한 변수

def hansu(x):
    xn = int(x) # x의 int형
    xs = str(x) # x의 str형
    if xn < 10:
        return True
    elif 10 <= xn and xn < 100:
        return True
    else:
        a = int(xs[2]) - int(xs[1])
        b = int(xs[1]) - int(xs[0])
        if a == b:
            return True
        else:
            return False

for i in range(1, n + 1):
    if hansu(i) == True:
        cnt += 1

print(cnt)
