class node(object):
    def __init__(self, k):
        self.key = k
        self.next = None


def bucket_sort(a_list):
    """用链表的形式"""
    h = []
    for i in range(0, 10):
        h.append(node(0))
    for i in range(0, len(a_list)):
        tmp = node(a_list[i])
        map = a_list[i] // 10
        p = h[map]
        if p.key == 0:
            h[map].next = tmp
            h[map].key = h[map].key + 1
        else:
            while p.next is not None and p.next.key <= tmp.key:
                p = p.next
            tmp.next = p.next
            p.next = tmp
            h[map].key = h[map].key + 1
    k = 0
    for i in range(0, 10):
        q = h[i].next
        while q:
            a_list[k] = q.key
            k = k + 1
            q = q.next
    return a_list


def main():
    a_list = [1, 4, 3, 23, 45, 97, 22, 10, 4]   # 桶排序测试代码
    a_list = bucket_sort(a_list)
    print(a_list)


if __name__ == '__main__':
    main()
