# TLE
from itertools import product

N, M = map(int, input().split())
A = list(map(int, input().split()))
A2 = [a**2 for a in A]

flag = "No"
for res in product(A2, repeat=4):
    if sum(res) == M:
        flag = "Yes"

print(flag) 




