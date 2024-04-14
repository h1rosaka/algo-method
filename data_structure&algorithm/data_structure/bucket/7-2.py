N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 100001(Nの上限)
counter = [0 for _ in range(100001)]


total = 0

# O(N)
for a in A:
    counter[a] += 1
    total += a

# O(Q*...)
for _ in range(Q):
    query = list(map(int, input().split()))

    # O(1)
    if query[0]==0:
        v = query[1]
        counter[v] += 1
        total += v
    
    # O(1)
    elif query[0]==1:
        x = query[1]
        y = query[2]
        total += (y-x) * counter[x]
        counter[y] += counter[x]
        counter[x] = 0

    # 100001（Nの上限）
    else:
        print(total)


