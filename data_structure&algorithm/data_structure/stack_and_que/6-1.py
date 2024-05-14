N = int(input())
S = input()
Q = int(input())


open_brackets = []
who_is_my_partner = [-1 for _ in range(N)]

for i in range(N):
    if S[i] == "(":
        open_brackets.append(i) #i番目に入っていた"("はまだ空いてますよ
    else:
        who_is_my_partner[i] = open_brackets.pop()
        who_is_my_partner[who_is_my_partner[i]] = i


for _ in range(Q):
    k = int(input())
    print(who_is_my_partner[k])