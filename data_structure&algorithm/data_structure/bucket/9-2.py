# これでもTLE
from itertools import combinations_with_replacement

N, M = map(int, input().split())
A = list(map(int, input().split()))
A2 = [a**2 for a in A]


flag = "No"
# 足りない場合
if max(A2)*4 < M:
    print(flag)
# 多すぎる場合
elif min(A2)*4 > M:
    print(flag)
# それ以外
else:
    for res in combinations_with_replacement(A2, r=4):
        if sum(res) == M:
            flag = "Yes"
    print(flag) 




