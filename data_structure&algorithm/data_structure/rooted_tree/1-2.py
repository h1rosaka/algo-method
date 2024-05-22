N = int(input())
parent_of_this_person_bucket = [0] + list(map(int, input().split()))
Q = int(input())



children_list_of_this_person_bucket = [[] for _ in range(N)]
for i in range(1,N):
    # 僕の親の"子供リスト"に僕を入れます
    parent = parent_of_this_person_bucket[i]
    children_list_of_this_person_bucket[parent].append(i)

for _ in range(Q):
    v = int(input())
    parent_of_v = parent_of_this_person_bucket[v]
    print(*children_list_of_this_person_bucket[parent_of_v])
