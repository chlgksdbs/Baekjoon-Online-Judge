dice = input().split(' ')
a = int(dice[0])
b = int(dice[1])
c = int(dice[2])

if a == b and b == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
elif c == a:
    print(1000 + (c * 100))
else:
    if a > b:
        if a > c:
            print((a * 100))
        else:
            print((c * 100))
    else:
        if b > c:
            print((b * 100))
        else:
            print((c * 100))
