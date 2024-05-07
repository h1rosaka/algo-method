from collections import defaultdict

N = int(input())
S = list(input().split())

counter = defaultdict(int)

for s in S:
    sorted_s = "".join(sorted(s))
    counter[sorted_s] += 1

anag_cnt = 0
for val in counter.values(): 
    # valC2
    anag_cnt += val * (val-1) / 2 

#全パターン
total_pattern = N * (N-1) / 2
print(anag_cnt/total_pattern)



