# 標準入力から値を受け取る
# num: int 型
num = int(input())

# 果物の名をキーとし、対応する値段を値とする辞書型の変数
fruits_dict = {
    "apple": 120, "banana": 100, "peach": 150, "lemon": 90,
    "grape": 140, "orange": 80, "melon": 200, "pineapple": 160,
}

# ここにコードを書いてください
most_expensive_fruits_so_far = "empty"
most_expensive_price_so_far = 0
for k, v in fruits_dict.items():
    if v > num:
        continue
    else:
        if v > most_expensive_price_so_far:
            most_expensive_fruits_so_far = k
            most_expensive_price_so_far = v


print(most_expensive_fruits_so_far)        