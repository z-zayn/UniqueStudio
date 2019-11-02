class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def insert(self, root, val):
        """二叉搜索树插入操作"""
        if root is None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def find(self, root, val):
        """查找操作"""
        if root is None:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.find(root.left, val)
        elif val > root.val:
            return self.find(root.right, val)

    def find_min(self, root):
        """查找二叉搜索树中最小值点,在删除节点时要用到"""
        if root.left:
            return self.find_min(root.left)
        else:
            return root

    def delete(self, root, val):
        """删除值为val的节点"""
        if root is None:
            print("没有值为%d的节点\n" % val)
            return
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
        else:
            if root.left and root.right:
                # 既有左子树又有右子树，则需找到右子树中最小值节点
                temp = self.find_min(root.right)
                root.val = temp.val
                # 再把右子树中最小值节点删除
                root.right = self.delete(root.right, temp.val)
            elif root.right is None and root.left is None:
                # 左右子树都为空
                root = None
            elif root.right is None:
                # 只有左子树
                root = root.left
            elif root.left is None:
                # 只有右子树
                root = root.right
        return root

    def print_tree(self, root):
        """打印二叉搜索树(中序打印，有序数列)"""
        if root is None:
            return
        self.print_tree(root.left)
        print(root.val, end=' ')
        self.print_tree(root.right)


def main():
    root = TreeNode(9)
    bst = BinarySearchTree()
    for i in range(10):
        # 插入
        root = bst.insert(root, 2*i)

    bst.print_tree(root)
    print("")
    # 查找
    print(bst.find(root, 6))
    print(bst.find(root, 11))
    print(bst.find(root, 12))
    # 删除
    root = bst.delete(root, 4)
    root = bst.delete(root, 9)
    root = bst.delete(root, 11)
    bst.print_tree(root)


if __name__ == '__main__':
    main()
