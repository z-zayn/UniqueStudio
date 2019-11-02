class UnionFind(object):
    def __init__(self, size):
        self.uf = list()        # 父节点列表
        self.rank = list()      # 秩列表

        for i in range(size):   # 初始化
            self.uf.append(i)

        for i in range(size):
            self.rank.append(0)

    def find(self, x):
        if x != self.uf[x]:
            # 如果父节点不是自己就递归查找
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def merge(self, x, y):
        if self.find(x) == self.find(y):
            # 判断x, y是否属于同一个集合
            print("%d和%d属于同一个集合不能合并" % (x, y))
            return
        else:
            x_f = self.find(x)
            y_f = self.find(y)
            if self.rank[x_f] > self.rank[y_f]:
                # 按秩合并
                self.uf[y_f] = x_f
            else:
                self.uf[x_f] = y_f
                if self.rank[x_f] == self.rank[y_f]:
                    self.rank[y_f] += 1


def main():
    union_find = UnionFind(10)
    union_find.merge(1, 2)
    union_find.merge(2, 3)
    union_find.merge(1, 4)
    print(union_find.find(4))
    union_find.merge(5, 6)
    union_find.merge(5, 7)
    union_find.merge(5, 8)
    union_find.merge(5, 9)
    union_find.merge(1, 5)
    print(union_find.find(8))
    print(union_find.find(4))


if __name__ == '__main__':
    main()