from UnionFind import *
edges = [
    [0, 1, 6],
    [0, 2, 1],
    [0, 3, 5],
    [2, 1, 5],
    [2, 3, 5],
    [2, 4, 5],
    [2, 5, 4],
    [1, 4, 3],
    [4, 5, 6],
    [5, 3, 2]
]


def kruskal(eds):
    uf = UnionFind(6)
    eds = sorted(eds, key=lambda x: x[-1])  # 按路径长度排序
    mst_edges, num = [], 0
    for edge in eds:
        if uf.find(edge[0]) != uf.find(edge[1]):    # 如果不构成回路
            mst_edges.append(edge)
            uf.merge(edge[0], edge[1])
            num += 1
        else:
            continue
        if num == 6:
            break
    return mst_edges


def main():
    mst_edges = kruskal(edges)
    for edge in mst_edges:
        print(edge)


if __name__ == '__main__':
    main()
