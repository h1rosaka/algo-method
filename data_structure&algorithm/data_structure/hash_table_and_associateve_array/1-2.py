N = int(input())
S = list(input().split())
Q = int(input())

def hash30(origninal_string):
    hashed_value_of_the_string = 0

    for i in range(len(origninal_string)):
        reverse_ith_index = -(1+i) # 後ろからi番目
        character = origninal_string[reverse_ith_index]
        n = ord(character) - ord("a") + 1
        hashed_value_of_the_string += n * (30**i)

    return hashed_value_of_the_string

maxval = 30**4 # 厳密にはもう少し下までしかいかない。

# カウンタバケットを埋める
counter = [0 for _ in range(maxval)]
for s in S:
    hashed_s = hash30(s)
    counter[hashed_s] += 1

for _ in range(Q):
    T = input()
    hashed_T = hash30(T)
    print(counter[hashed_T])



