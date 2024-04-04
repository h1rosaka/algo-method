# 標準入力から値を受け取る
# S: str 型
S = input()
name_list = S.split(sep=" ")

# 受け取った値を利用してコードを書いてください

ans = name_list[1][0].lower() + "_" + (name_list[0]).lower()
print(ans)
