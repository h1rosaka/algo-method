#このままだとTLE

N = int(input())
A = list(map(int, input().split()))
Q = int(input())


# O(1)
def insert(v):
    A.append(v)

# O(N)
def return_A_after_delete(v):
    new_A = []
    for a in A:
        if a != v:
            new_A.append(a)
    return new_A
    
# O(N)
def count(v):
    count_bucket = [0 for _ in range(100001)]
    for a in A:
        count_bucket[a] += 1
    print(count_bucket[v])



for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]
    v = query[1]

    if query_type == 0:
        insert(v)

    elif query_type == 1:
        A = return_A_after_delete(v)
    else:
        count(v)
