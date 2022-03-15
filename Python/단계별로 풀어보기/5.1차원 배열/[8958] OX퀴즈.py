n = int(input())

for i in range(n):
    score = 0
    plus = 1
    quiz = input()
    for j in range(len(quiz)):
        if quiz[j] == 'O':
            score += plus
            plus += 1
        else:
            plus = 1
    print(score)
