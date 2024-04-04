N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# for i in range()

# AとBからそれぞれ一個ずつ取ってきて、Aから取ってきた方の方が大きかった時だけOK
cnt = 0
for a in A:
    for b in B:
        if a>b:
            cnt += 1

print(cnt)