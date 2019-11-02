from queue import PriorityQueue
_edges = [              # 路径长度在列表的开头
    [6, 0, 1],
    [1, 0, 2],
    [5, 0, 3],
    [5, 2, 1],
    [5, 2, 3],
    [5, 2, 4],
    [4, 2, 5],
    [3, 1, 4],
    [6, 4, 5],
    [2, 5, 3]
]


def prim(s, edges):
    q = PriorityQueue()
    mst_edges = list()
    visited = dict()
    for i in range(6):
        visited[i] = False      # 初始化标记字典
    v = s
    visited[v] = True
    for edge in edges:
        if v == edge[1] or v == edge[2]:    # 将v点所有能到达点的路径入队列
            q.put(edge)
    while not q.empty():
        next = q.get()
        if visited[next[2]] is True:        # 如果目标点访问过
            continue
        else:
            mst_edges.append(next)
            visited[next[2]] = True
            for edge in edges:
                if next[2] == edge[1] or next[2] == edge[2]:
                    q.put(edge)
    return mst_edges


def main():
    new_edges = sorted(_edges, key=lambda x: x[0])  # 按路径长度排序
    mst_edges = prim(new_edges[0][1], new_edges)
    for edge in mst_edges:
        print(edge)


if __name__ == '__main__':
    main()
