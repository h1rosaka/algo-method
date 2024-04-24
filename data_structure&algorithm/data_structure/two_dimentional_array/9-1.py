N, Q = map(int, input().split())


# 内側のリストは、ユーザーiをfollowしている人だけ1が入るようにする
follow_relation = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        x = query[1]
        y = query[2]
        follow_relation[y][x] = 1
    else:
        z  = query[1]
        follower_cnt = 0
        for i in range(len(follow_relation[z])):
            if follow_relation[z][i] == 1:
                print(i, end=" ")
                follower_cnt += 1
        if follower_cnt == 0:
            print("No")
        print("")