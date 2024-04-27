N, Q = map(int, input().split())

front = [-1 for i in range(N)]
back = [-1 for i in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        p = query[1]
        q = query[2]
        back[p] = q
        front[q] = p
    else:
        r = query[1]
        # rの前側に車両がある場合、その車両も影響受けるので情報の更新
        front_car = front[r]
        if front_car != -1:
            back[front_car] = back[r]
        # rの後ろ側に車両がある場合、その車両も影響受けるので情報の更新
        back_car = back[r]
        if back_car != -1:
            front[back_car] = front[r] 

        # rの前後をなくしておく
        front[r] = -1
        back[r] = -1



#前にいる車両を数える
front_cnt = 0
current = 0
while current != -1:
    # print(current)
    front_cnt += 1
    current = front[current]
   
#後ろも
back_cnt = 0
current = 0
while current != -1:
    # print(current)
    back_cnt += 1
    current = back[current]

total_car_cnt = front_cnt + back_cnt -1
print(total_car_cnt)
