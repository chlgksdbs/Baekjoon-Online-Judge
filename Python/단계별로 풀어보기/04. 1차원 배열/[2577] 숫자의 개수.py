a = int(input())
b = int(input())
c = int(input())

sum = a * b * c
count = []

for i in range(10):
    print(str(sum).count(str(i)))
# list속의 특정 숫자나 문자의 개수를 세는 법은 count() 함수를 사용한다. 단, 이 문제에서는 int -> str형으로 변환했기 때문에, count()내부에 숫자 i가 아닌 str형으로 변환한 i를 사용한다.
