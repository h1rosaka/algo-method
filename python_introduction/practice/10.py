study_info = [
    {"name": "aruru", "subject": "math", "time": 30},
    {"name": "iruru", "subject": "science", "time": 65},
    {"name": "aruru", "subject": "science", "time": 20},
    {"name": "ururu", "subject": "math", "time": 45},
    {"name": "iruru", "subject": "english", "time": 10},
    {"name": "ururu", "subject": "science", "time": 15},
    {"name": "aruru", "subject": "english", "time": 30},
    {"name": "ururu", "subject": "english", "time": 25},
    {"name": "iruru", "subject": "math", "time": 20}
]

# 人ごとに勉強時間の合計を記録する辞書型変数
sum_person = {
    "aruru": 0, "iruru": 0, "ururu": 0
}

# 科目ごとに勉強時間の合計を記録する辞書型変数
sum_subject = {
    "math": 0, "science": 0, "english": 0
}

# ここに sum_person, sum_subject を編集するコードを書いてください

# 正解の計算
for dictionary in study_info:

    who = dictionary["name"]
    what = dictionary["subject"]
    how_long = dictionary["time"]

    sum_person[who] += how_long
    sum_subject[what] += how_long




# 答えを出力
print(sum_person)
print(sum_subject)