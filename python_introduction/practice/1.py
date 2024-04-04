# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
new_s = ""

for character in S:
    # 小文字の子音(not母音)だった時だけ置き換える
    if character.islower() and character not in ["a","i","u","e","o"] and character:
        character = "_"
    
    new_s += character

print(new_s)
