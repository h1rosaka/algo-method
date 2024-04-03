import datetime # datetime モジュールを読み込む

# 2123 年 3 月 28 日を表す変数
d = datetime.date(2123, 3, 28)

# ここにコードを書いてください
ans = "No"
if d.weekday() == 6:
    ans = "Yes"
print(ans)