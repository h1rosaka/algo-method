N = int(input())
parent_bucket = [-1] + list(map(int, input().split())) #始祖の人には親がいない
Q = int(input())


# 子供がわかるバケットも欲しい
children_bucket = [[] for _ in range(N)]
for i in range(1,N):
    parent = parent_bucket[i]
    children_bucket[parent].append(i)


for _ in range(Q):
    v = int(input())
    parent_of_v = parent_bucket[v]
    print(*children_bucket[parent_of_v])
