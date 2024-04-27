# TLE
class Node:
    def __init__(self, value=""):
        self.nex = None
        self.prev = None
        self.value = value


def connect(p,q):
    p.nex = q 
    q.prev = p


def contract(r):
    if r.prev != None:
        r.prev.nex = r.nex
    if r.nex != None:
        r.nex.prev = r.prev

N, Q = map(int, input().split())

trains = [Node(i) for i in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        p = query[1]
        q = query[2]
        p_node = trains[p]
        q_node = trains[q]
        connect(p_node, q_node)
    else:
        r = query[1]
        r_node = trains[r]
        contract(r_node)


current_node = trains[0]
count_back = 0
while current_node.nex != None:
    count_back += 1
    current_node = current_node.nex

current_node = trains[0]
count_front = 0
while current_node.prev != None:
    count_back += 1
    current_node = current_node.prev


print(1 + count_back + count_front)
