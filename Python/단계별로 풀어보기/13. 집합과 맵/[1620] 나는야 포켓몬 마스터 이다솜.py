# n : 도감에 수록되어 있는 포켓몬의 개수, m : 맞춰야 하는 문제의 개수
n, m = map(int, input().split())
pokemon = []
for i in range(n): # 입력
    pokemon.append(input())

for _ in range(m): # 출력
    sol = input()
    solInt = 0 # 값이 0이면 문자열, 1이면 int형

    if sol.isnumeric(): # 입력에 숫자만 포함 된 경우, int형으로 변환
        sol = int(sol)
        solInt = 1
    
    if solInt == 1:
        print(pokemon[sol - 1]) # 인덱스 접근은 0부터 시작하므로 1을 뺀다.
    else:
        print(pokemon.index(sol) + 1) # 도감 번호는 1부터 시작하므로 1을 더한다.