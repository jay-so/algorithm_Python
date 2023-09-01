#1.시험 본 과목의 갯수 N
N = input()

#2.현재 성적
score = list(map(int,input().split()))
maxScore= max(score)
sum = sum(score)

print(sum * 100 /maxScore/int(N))
