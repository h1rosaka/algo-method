H, W = map(int, input().split())

S = ""
T = ""
diff_cnt = 0
for _ in range(H):
    S += input()


for _ in range(H):
    T += input()

for i in range(H * W):
    if S[i] != T[i]:
        diff_cnt += 1
print(diff_cnt)