N = int(input())
S = input()

my_list = []

counter = 0
for s in S:
    if s == "(":
        my_list.append("(")
    else:
        my_list.pop()

    if len(my_list) == 0:
        print(counter)
        break
    counter += 1