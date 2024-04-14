# AC
N = int(input())
A = list(map(int, input().split()))
Q = int(input())


count_bucket = [0 for _ in range(100001)]

# 最初に入っている要素の数を数えておく
for a in A:
    count_bucket[a] += 1


# O(1)
def insert(v):
    count_bucket[v] += 1
# O(1)
def delete(v):
    count_bucket[v] = 0 
# O(1)
def count(v):
    print(count_bucket[v])

for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]
    v = query[1]

    if query_type == 0:
        insert(v)

    elif query_type == 1:
        delete(v)
    else:
        count(v)
