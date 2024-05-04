N = int(input())
S = list(input().split())
Q = int(input())


counter = {}
for s in S:
    counter[s] = counter.get(s,0) + 1


for _ in range(Q):
    query = list(input().split())
    q_type = query[0]
    T = query[1]

    if q_type == "0":
        counter[T] = counter.get(T, 0) + 1
    elif q_type == "1":
        counter[T] = 0
    else:
        print(counter.get(T,0))

