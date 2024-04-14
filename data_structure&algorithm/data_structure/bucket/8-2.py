# 二重ループなくしたけどまだTLE

import math
Q = int(input())


# candidate_nums = [x for x in range(-100,101)]
square_of_candidate_nums = [x**2 for x in range(-100,101)]

count_square_of_candidate_nums = [0 for _ in range(10001)]

for square_of_candidate_num in square_of_candidate_nums:
    count_square_of_candidate_nums[square_of_candidate_num] += 1



for _ in range(Q):
    cnt = 0
    p = int(input())

    for i in range(len(square_of_candidate_nums)):
        square_of_checking_target = square_of_candidate_nums[i]

        if p - square_of_checking_target in square_of_candidate_nums:
            cnt += count_square_of_candidate_nums[p - square_of_checking_target]


    print(cnt)
    # print(candidate_nums[99])

