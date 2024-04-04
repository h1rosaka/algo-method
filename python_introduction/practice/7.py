# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
number_dict = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

ans = ""


while len(S) > 0:

    if S[0:3] in number_dict:
        ans += number_dict[S[0:3]]
        S = S[3:]

    elif S[0:4] in number_dict:
        ans += number_dict[S[0:4]]
        S = S[4:]

    else:
        ans += number_dict[S[0:5]]
        S = S[5:]

print(ans)