N = int(input())




w_list = input().split()
w_concat = "".join(w_list)

alphabet_cnt = [0 for _ in range(ord("z")+1)]

for character in w_concat:
    alphabet_cnt[ord(character)] += 1

flg = True
for cnt in alphabet_cnt[ord("a"):ord("z")+1]:
    if cnt == 0:
        flg = False

if flg:
    print("Yes")
else:
    print("No")