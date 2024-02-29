# 리스트
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 인덱스 4, 즉 다섯번째 원소에 접근
print(a[4])

# 빈 리스트 선언 방법 1
a = list()
print(a)

# 빈 리스트 선언 방법 2
a = []
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = 7
print(a)

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# 리스트 컴프리헨션 - 리스트 초기화
# 0 부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1 부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]

print(array)
