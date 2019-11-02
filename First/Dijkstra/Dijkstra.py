from heapq import heappop, heappush

w = [                           # 顶点间距离, -1表示无穷大
    [0,  7,  9, -1, -1, 14],
    [7,  0, 10, 15, -1, -1],
    [9, 10,  0, 11, -1,  2],
    [-1, 15, 11,  0,  6, -1],
    [-1, -1, -1,  6,  0,  9],
    [14, -1,  2, -1,  9,  0]
]


def dijkstra(start, dest):
    n = 6                           # 顶点数
    visited = list()                # 标记顶点是否已确定
    q = [(0, start, str(start))]    # 路径长, 序号, 路径

    while q:    # 当Q非空
        d, u, p = heappop(q)
        if u == dest:
            print(d, p)
            break       # 在找到目的地之后终止
        if u not in visited:
            visited.append(u)
            v_reached_from_u = [i for i in range(n) if w[u][i] != -1]   # u能到达的顶点
            for v in v_reached_from_u:
                if v not in visited:
                    heappush(q, ((d + w[u][v]), v, ''.join((p, '->', str(v)))))   # 到顶点v的某条路径的距离


def main():
    # start = int(input())
    # dest = int(input())
    dijkstra(0, 5)


if __name__ == '__main__':
    main()
