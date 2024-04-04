S = input()
N = int(input())

# S[N]はN=1の時に2番目を出してしまうので、-1
print(S[N-1])