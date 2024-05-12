X = input()
N = int(input())
S = list(input().split())

que = []

tail = 0

for s in S:
    if s == "+":
        new_val = que[tail-2] + que[tail -1]
        que.pop()
        que.pop()
        que.append(new_val)
        tail -= 1 

    elif s == "-":
        new_val = que[tail-2] - que[tail -1]
        que.pop()
        que.pop()
        que.append(new_val)
        tail -= 1

    elif s =="*":
        new_val = que[tail-2] * que[tail -1]
        que.pop()
        que.pop()
        que.append(new_val)
        tail -= 1

    else:
        que.append(int(s))
        tail += 1

print(X+"="+str(que[0]))