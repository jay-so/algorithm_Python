# 1.n을 입력 받음
n = input()

# 2. 숫자를 입력 받음
numbers = list(input())

sum = 0;

# 3. for문을 통해 리스트에 저장된 숫자들의 합을 구함
for i in numbers:
    sum += int(i)

print(sum)
