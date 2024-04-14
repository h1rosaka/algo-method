N = int(input())
A = list(map(int, input().split()))


#バケットで数える
count_bucket = [0 for _ in range(5*(10**5)+1)]

# バケットにカウントした数字入れる
for a in A:
    count_bucket[a] += 1

max_cnt = 0
for i in range(len(count_bucket)):
    cnt_num = count_bucket[i]
    if cnt_num > max_cnt:
        max_cnt = cnt_num
        max_cnt_idx = i

print(max_cnt_idx) 