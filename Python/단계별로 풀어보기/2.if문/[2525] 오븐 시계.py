a = input().split(' ')
x = int(a[0])
y = int(a[1])
b = int(input())

h = b // 60
m = b % 60

if x + h < 24:
    if y + m < 60:
        print((x + h), (y + m), end=" ")
    else:
        if x + h < 23:
            print((x + h + 1), (y + m - 60), end=" ")
        else:
            print('0', (y + m - 60), end=" ")
else:
    if y + m < 60:
        print((x + h - 24), (y + m), end=" ")
    else:
        print((x + h - 23), (y + m - 60), end=" ")
