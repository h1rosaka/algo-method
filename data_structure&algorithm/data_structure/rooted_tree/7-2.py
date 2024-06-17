#どこかにミスがある。　global調べてみる
N = int(input())
A = [-1] + list(map(int, input().split()))
Q = int(input())

children = [[] for _ in range(N)]
for i in range(1,N):
    children[A[i]].append(i)

count = 0
def rec(v):
    global count
    count += 1
    print("aaa", count)
    for nv in children[v]:
        rec(nv)
    count -= 1 #jibun


rec(0)
print(count)
for _ in range(Q):
    v = int(input())
    # count = 0
    rec(v)
    print(count)