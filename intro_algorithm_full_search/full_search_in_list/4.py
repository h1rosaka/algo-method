N, V = map(int, input().split())
A = list(map(int, input().split()))

order = -1

for i in range(len(A)):
    if A[i] == V:
        order = i

print(order)