N = int(input())
S = input()

open_brackets = []


flg = "Yes"
for i in range(N):
    if S[i] == "(":
        open_brackets.append(i)
    else:
        if len(open_brackets) >= 1:
            open_brackets.pop()
        else:
            flg = "No"
            break
            # (が左にないのに)が来ちゃった、Noパターンその1

# open bracketを消しきれなかったNoパターンその2
if len(open_brackets) != 0:
    flg = "No"

print(flg)