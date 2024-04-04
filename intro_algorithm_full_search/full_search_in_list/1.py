N, V = map(int, input().split())
A = list(map(int, input().split()))

flag= "No"
for a in A:
    if a == V:
        flag ="Yes"

print(flag)