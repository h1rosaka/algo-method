# defaultdict使わずにdictで実装してみる



N = int(input())
A = list(map(int, input().split()))
Q = int(input())

student_count_by_score = dict()

# create dict 
for i in range(len(A)):
    score_string = str(A[i])
    student_count_by_score[score_string] = student_count_by_score.get(score_string, 0) + 1

# answer to the queries
for j in range(Q):
    x = input() # x is string
    count = student_count_by_score.get(x, 0)
    print(count)



