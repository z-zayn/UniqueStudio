class MyQueue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, node):
        # 压入
        self.stack1.append(node)

    def if_empty(self):
        # 判断队列是否为空
        if len(self.stack1) != 0 or len(self.stack2) != 0:
            return False
        else:
            return True

    def pop(self):
        # 弹出
        if len(self.stack2) == 0:   # 2为空时就把1中所有的都弹出再压入2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()    # 2不空的时候最顶上的位置就是应该最先进入队列的元素


def main():
    queue = MyQueue()
    for i in range(5):
        queue.push(i)

    print(queue.pop())
    print(queue.pop())
    queue.push(5)
    queue.push(6)
    while queue.if_empty() is False:
        print(queue.pop())


if __name__ == '__main__':
    main()


