N = int(input())
A = list(map(int, input().split()))


counter = [0 for _ in range(100001)]
a_set = set()

for a in A:
    counter[a] += 1
    a_set.add(a)

total_num_ways = 0

# 同じ整数二つを選ぶ方法の数
# 1種類目の整数の場合、2種類目の整数の場合、、、
for a in a_set:
    num_ways = counter[a]*(counter[a]-1)
    total_num_ways += num_ways

# 適当に二つ選ぶ方法の数
# N * (N-1)

probability = total_num_ways/ (N*(N-1))
print(probability)