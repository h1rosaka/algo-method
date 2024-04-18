N, M = map(int, input().split())
A = list(map(int, input().split()))





# ２つ足した結果として現れる可能性があるかどうか
# Mが10^6なのでその範囲で見る
is_this_num_possible = [0 for _ in range((2*10**6))]

for a in A:
    for b in A:
        total = a**2 + b**2 
        is_this_num_possible[total] = 1



flag = "No"
for possible_total_candidate in range(len(is_this_num_possible)):
    if is_this_num_possible[possible_total_candidate]==1 and is_this_num_possible[M - possible_total_candidate] == 1:
        flag = "Yes"

print(flag)




