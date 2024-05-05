N = int(input())
S = list(input().split())

string_set = set()
for s in S:
    string_set.add(s)
print(len(string_set))