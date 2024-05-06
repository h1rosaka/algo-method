from collections import defaultdict
N, Q = map(int, input().split())



# is_follower_of[x]で、xのfollowerかどうかがわかる配列を取得できる
is_follower_of = [[0 for _ in range(N)] for _ in range(N)]


counter = defaultdict(int)
#最初は全員誰にもフォローされてない状態なので、それのカウントを入れておく
counter[tuple([0 for _ in range(N)])] = N

for _ in range(Q):
    query = list(map(int, input().split()))


    if query[0] == 0:
        x = query[1]
        y = query[2]
        if is_follower_of[y][x] == 1:
            continue
        counter[tuple(is_follower_of[y])] -= 1
        is_follower_of[y][x] = 1
        counter[tuple(is_follower_of[y])] += 1

    elif query[0] == 1:
        x = query[1]
        y = query[2]
        if is_follower_of[y][x] == 0:
            continue
        counter[tuple(is_follower_of[y])] -= 1
        is_follower_of[y][x] = 0
        counter[tuple(is_follower_of[y])] += 1

    else:
        z = query[1]
        print(counter[tuple(is_follower_of[z])]-1)