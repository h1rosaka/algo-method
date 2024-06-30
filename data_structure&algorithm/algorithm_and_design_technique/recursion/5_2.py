num_available_numbers, desired_total = map(int, input().split())
numbers_list = list(map(int,input().split()))

import sys
sys.setrecursionlimit(10**6)


#前からN個でどうか→N-1こでどうか、→..0個でどうか
def func(i, desired_total):
    if i == 0:
        if desired_total == 0:
            flag = True
        else:
            flag = False
        return flag
        
    else:
        flag = False
        # 一個前までで既に作れている
        if func(i-1, desired_total):
            flag = True
        # 今回来たやつ入れてピッタリ
        if func(i-1, desired_total - numbers_list[i-1]):
            flag = True      
        return flag



if func(num_available_numbers, desired_total):
    print("Yes")
else:
    print("No")