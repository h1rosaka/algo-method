#TLE

from itertools import combinations_with_replacement
N, M = map(int, input().split())
A = list(map(int, input().split()))

max_val = (10**8)*2
sum_bucket = [0 for _ in range(max_val+1)]

for comb in combinations_with_replacement(A,2):
    two_square_sum = comb[0]**2 + comb[1]**2
    sum_bucket[two_square_sum] = 1

flg = "No"

for i in range(max_val+1):
    if sum_bucket[i] == 0:
        continue
    if sum_bucket[M - i] == 1:
        flg = "Yes"
print(flg)
