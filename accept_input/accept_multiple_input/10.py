S = input()
N, M = map(int, input().split())

new_s = [c for c in S]
new_s[N-1] = S[M-1]
new_s[M-1] = S[N-1]

print("".join(new_s))