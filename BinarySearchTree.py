class BSTNode:
    def __init__(self, data):
        """
        General node class implementation
        :param data:
        """
        self.val = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None
        self.nodeSum = 0
        self.wbf = []

    def insert(self, x):
        """
        Insert Item into Tree
        :param x:
        :return:
        """
        new_node = BSTNode(x)

        # Base Case
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            done = False

            # Iterative implemetation of inserting a node
            while not done:
                if x > current.val:
                    if current.right is None:
                        current.right = new_node
                        self.size += 1
                        done = True
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = new_node
                        self.size += 1
                        done = True
                    else:
                        current = current.left

    def totalHeight(self, root):
        """
        Auxiliary function for getTotalHeight
        :param root:
        :return:
        """
        if root is None:
            return -1
        leftheight = self.totalHeight(root.left)
        rightheight = self.totalHeight(root.right)
        height = max(leftheight, rightheight) + 1
        self.nodeSum += height
        return height

    def getTotalHeight(self):
        """
        Find sum of all heights of nodes of a tree
        :return:
        """
        self.nodeSum = 0
        self.totalHeight(self.root)
        return self.nodeSum

    def weightBalanceFactor(self, node):
        """
        Auxilary function to the find the weight balance factor of the tree node
        :param node:
        :return:
        """

        # Base case
        if node is None:
            return 0
        absdif = abs(self.weightBalanceFactor(node.left) - self.weightBalanceFactor(node.right))
        self.wbf.append(absdif)
        return 1 + self.weightBalanceFactor(node.left) + self.weightBalanceFactor(node.right)

    def getWeightBalanceFactor(self):
        """
        Find the weight balance factor of a tree node.
        :return:
        """
        self.wbf = []
        self.weightBalanceFactor(self.root)
        return max(self.wbf)


if __name__ == "__main__":
    my_bst = BinarySearchTree()
    my_bst.insert(1)
    my_bst.insert(9)
    my_bst.insert(12)
    my_bst.insert(4)
    my_bst.insert(3)
    print(my_bst.getTotalHeight())
    print(my_bst.getWeightBalanceFactor())