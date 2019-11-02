g = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
order = list()
out_zero = list()
visited = list()


def visit(gr, n):
    if n not in visited:
        visited.append(n)
    for m in range(1, len(gr)):
        if gr[m][n] and m not in visited:
            visit(gr, m)
    # 核心之处，待理解
    order.insert(0, n)


def main():

    for i in range(1, len(g)):
        if g[i].__eq__([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            out_zero.append(i)

    for n in out_zero:
        visit(g, n)
    print('拓扑排序：')
    print(order)


if __name__ == '__main__':
    main()
