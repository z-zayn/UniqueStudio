class Map(object):
    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        """加节点"""
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        """增加边，类似邻接链表"""
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if u != v:
                self.node_neighbors[v].append(u)

    def nodes(self):
        """看当前有哪些节点"""
        return self.node_neighbors.keys()

    # 递归DFS
    def depth_first_search(self, root=None):
        order = list()

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if n not in self.visited:
                    dfs(n)

        if root:
            dfs(root)

        # 对于不连通的结点（即dfs（root）完仍是没有visit过的单独处理，再做一次dfs
        for node in self.nodes():
            if node not in self.visited:
                dfs(node)
        self.visited = {}
        print(order)
        return order

    # 非递归DFS
    def depth_first_search2(self, root=None):
        """
        利用栈实现
        从源节点进栈然后弹出
        每弹出一个节点就将与它相邻且没进过栈的一个节点压入栈中
        直到栈空
        """
        stack = []
        order = []

        def dfs():
            while stack:
                node = stack[-1]    # 取栈顶元素
                for n in self.node_neighbors[node]:  # 遍历邻接节点
                    if n not in self.visited:
                        order.append(n)
                        stack.append(n)
                        self.visited[n] = True
                        break           # 只压一个进栈
                else:
                    stack.pop()

        if root:
            stack.append(root)
            order.append(root)
            self.visited[root] = True
            dfs()

        for node in self.nodes():
            if node not in self.visited:
                stack.append(node)
                order.append(node)
                self.visited[node] = True
                dfs()

        self.visited = {}
        print(order)
        return order

    def breadth_first_search(self, root=None):
        """
        利用队列
        从源节点入队再出队
        每弹出一个节点就将它所有的没入过队的邻接点入队
        直到队空
        """
        queue = []
        order = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (n not in self.visited) and (n not in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if node not in self.visited:
                queue.append(node)
                order.append(node)
                bfs()

        self.visited = {}
        print(order)
        return order


def main():
    m = Map()
    m.add_nodes([i + 1 for i in range(8)])
    m.add_edge((1, 2))
    m.add_edge((1, 3))
    m.add_edge((2, 4))
    m.add_edge((2, 5))
    m.add_edge((4, 8))
    m.add_edge((5, 8))
    m.add_edge((3, 6))
    m.add_edge((3, 7))
    m.add_edge((6, 7))
    print("nodes:", m.nodes())

    print("BFS：")
    order = m.breadth_first_search(1)
    # self.visited 在经历了一次bfs之后已经有了值，如果dfs直接进行，就会发生只输出结点1的情况
    print("递归DFS：")
    order = m.depth_first_search(1)
    print("非递归DFS")
    order = m.depth_first_search2(1)


if __name__ == '__main__':
    main()
