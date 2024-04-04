# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください

# 10文字だったとき、最後のスライスは[7:10] →iは7まで
nickname_set = set()
for i in range(len(S)-2):
   nickname_set.add(S[i:i+3])
print(len(nickname_set))