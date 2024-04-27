N = int(input())

# indexで検索できるようにしたいので、使わないindex=0もある
nex = [i+1 for i in range(N+1)]
prev = [i-1 for i in range(N+1)]

# 輪っかにするために１とNをつなげる
nex[N] = 1
prev[1] = N 

# N- 1回取り除く
target = 1
for _ in range(N-1):
    # 連結の輪から、targetを参照できないようにする
    prev[nex[target]] = prev[target]
    nex[prev[target]] = nex[target]

    # 次のターゲットを決める
    target = nex[nex[target]]

# 最後に残ったやつ
print(target)