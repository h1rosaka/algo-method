HEIGHT, WIDTH = map(int, input().split())
mymap = [input() for _ in range(HEIGHT)]
p, q = map(int, input().split())




def count_black_in_string(target_string):
    cnt = 0
    for character in target_string:
        if character == "#":
            cnt += 1
    return cnt


def count_black(p,q):

    vertical_chrs = "".join([string[q] for string in mymap])
    horizontal_chrs_except_itself = mymap[p][:q]+ mymap[p][q+1:]

    # upper_row_blk_cnt = count_black_in_string(mymap[p-1][q-1:q+2])
    # middle_row_blk_cnt = count_black_in_string(mymap[p][q-1] + mymap[p][q+1])
    # lower_row_blk_cnt = count_black_in_string(mymap[p+1][q-1:q+2])
    
    cnt = count_black_in_string(vertical_chrs+horizontal_chrs_except_itself)


    return cnt

# print(count_black_in_string(mymap[p][q-1] + mymap[p][q+1]))
print(count_black(p,q))