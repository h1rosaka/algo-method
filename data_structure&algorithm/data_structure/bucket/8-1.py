# TLE
import math
Q = int(input())


candidate_nums = [x for x in range(-100,101)]
square_of_candidate_nums = [x**2 for x in range(-100,101)]

cnt = 0

for _ in range(Q):
    myset = set()
    p = int(input())

    for i in range(len(candidate_nums)):
        square_of_checking_target = square_of_candidate_nums[i]
        for j in range(len(square_of_candidate_nums)):
            if p - square_of_checking_target == square_of_candidate_nums[j]:
                myset.add((i,j))        
    print(len(myset))
    # print(candidate_nums[99])

