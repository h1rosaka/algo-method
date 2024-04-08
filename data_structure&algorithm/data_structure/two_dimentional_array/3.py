H, W, x, y = map(int, input().split())

S = [[0 for _ in range(W)] for _ in range(H)]


for i in range(H):
    line = input()
    for j in range(W):
            S[i][j] = line[j]



print("".join(S[x-1][y-1:y+2]))
print("".join(S[x][y-1:y+2]))
print("".join(S[x+1][y-1:y+2]))


# print(*S[x-1][y-1:y+2])
# print(*S[x][y-1:y+2])
# print(*S[x+1][y-1:y+2])