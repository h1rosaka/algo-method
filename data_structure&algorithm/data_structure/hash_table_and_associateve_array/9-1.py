from itertools import combinations_with_replacement
N, M = map(int, input().split())
A = list(map(int, input().split()))


sum_square_set = set()

for comb in combinations_with_replacement(A,2):
    two_square_sum = comb[0]**2 + comb[1]**2
    sum_square_set.add(two_square_sum)

flg = "No"

for sum_square in sum_square_set:
    if M-sum_square in sum_square_set:
        flg = "Yes"
print(flg)