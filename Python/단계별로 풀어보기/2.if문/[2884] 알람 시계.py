a = input().split(' ')

h = int(a[0])
m = int(a[1])

if 60 > m >= 45:
    print(h, (m - 45), end=" ")
elif 45 > m >= 0:
    if h == 0:
        print(23, (60 - 45 + m), end=" ")
    else:
        print((h - 1), (60 - 45 + m), end=" ")
