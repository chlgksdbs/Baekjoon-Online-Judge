s = input() # 알파벳 대문자로 이루어진 단어
t = 0 # 다이얼을 걸기 위한 최소 시간

for i in s:
    if 'A' <= i and i <= 'C':
        t += 3
    elif 'D' <= i and i <= 'F':
        t += 4
    elif 'G' <= i and i <= 'I':
        t += 5
    elif 'J' <= i and i <= 'L':
        t += 6
    elif 'M' <= i and i <= 'O':
        t += 7
    elif 'P' <= i and i <= 'S':
        t += 8
    elif 'T' <= i and i <= 'V':
        t += 9
    elif 'W' <= i and i <= 'Z':
        t += 10

print(t)
