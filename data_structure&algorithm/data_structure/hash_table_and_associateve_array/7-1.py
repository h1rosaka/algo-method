N = int(input())
A = list(map(int, input().split()))


set_a = set(A)

print(len(A) - len(set(A)))

