L, R = map(int, input().split())

cnt = 0
for i in range(L, R+1):
    for j in range(i+1, R+1):
        if i%10 == j%10:
            cnt +=1
print(cnt)