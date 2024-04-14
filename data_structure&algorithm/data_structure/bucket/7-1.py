# TLE
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

counter = [0 for _ in range(100001)]
for a in A:
    counter[a] += 1


for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0]==0:
        v = query[1]
        counter[v] += 1
    
    elif query[0]==1:
        x = query[1]
        y = query[2]
        counter[y] += counter[x]
        counter[x] = 0

    else:
        total = 0
        for i in range(len(counter)):
            total += i*counter[i]

        print(total)



