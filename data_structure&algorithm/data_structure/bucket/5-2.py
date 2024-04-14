N, Q = map(int, input().split())


follower_cnt_bucket_matrix = [[0 for _ in range(N)] for _ in range(N)]
folloer_counter = [0 for _ in range(N)]


for _ in range(Q):
    query = list(map(int, input().split()))

    # O(1)
    if query[0] == 0:
        x = query[1]
        y = query[2]
        
        if follower_cnt_bucket_matrix[y][x] == 0:
            folloer_counter[y] += 1
            follower_cnt_bucket_matrix[y][x] = 1

    #O(1)
    elif query[0] == 1:
        x = query[1]
        y = query[2]
        if follower_cnt_bucket_matrix[y][x] == 1:
            folloer_counter[y] -= 1
            follower_cnt_bucket_matrix[y][x] = 0
    # O(1)
    else:
        z = query[1]
        print(folloer_counter[z])

