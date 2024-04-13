# バケットで実装する
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# create bucket
num_students_by_score = [0 for _ in range(100001)]

# run through A to count num students
for a in A:
    num_students_by_score[a] += 1

# print num students who got score x
for _ in range(Q):
    x = int(input())
    print(num_students_by_score[x])