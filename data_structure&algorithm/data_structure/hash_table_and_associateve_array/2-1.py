N = int(input())
S = list(input().split())
M = 1000003

def hash30(s):
    n_ary = 0

    for i in range(len(s)):
        character = s[-(i+1)] # 後ろからi番目
        c_i = ord(character) - ord("a") +1 # aが１
        n_ary += c_i * pow(30, i)

    hashed_s = n_ary % M

    return hashed_s

counter = [0 for _ in range(M)]
for s in S:
    counter[hash30(s)] += 1


print(max(counter))
N = int(input())
S = list(input().split())
M = 1000003

def hash30(s):
    n_ary = 0

    for i in range(len(s)):
        character = s[-(i+1)] # 後ろからi番目
        c_i = ord(character) - ord("a") +1 # aが１
        n_ary += c_i * pow(30, i)

    hashed_s = n_ary % M

    return hashed_s

counter = [0 for _ in range(M)]
for s in S:
    counter[hash30(s)] += 1


print(max(counter))
