numList = []
numSum = 0

for i in range(5):
    numList.append(int(input()))
    numSum += numList[i]

numList.sort()

print(numSum // 5)
print(numList[2])