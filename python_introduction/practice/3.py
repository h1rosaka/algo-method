from collections import defaultdict
# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
countdict = defaultdict(int)
new_s = ""
for character in S:
    countdict[f"{character}"] += 1
    if countdict[f"{character}"] >= 2:
        character = "*"
    new_s += character

print(new_s)
    