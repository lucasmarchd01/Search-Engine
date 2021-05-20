class AVLTreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTreeMap:
    def __init__(self):
        self.root = None

    def get(self, root, keyToFind):
        """
        Find a key value in a tree.
        :param root:
        :param keyToFind:
        :return:
        """

        # Tree is empty
        if root is None:
            return

        # Key is found
        elif root.key == keyToFind:
            return root.val

        # Traverse right
        elif root.key < keyToFind:
            return self.get(root.right, keyToFind)

        # Traverse left
        else:
            return self.get(root.left, keyToFind)

    def getHeight(self, node):
        """
        Return the height attribute of a node
        :param node: 
        :return: 
        """

        # No root
        if not node:
            return 0

        # Return the height attribute
        else:
            return node.height

    def getBalance(self, node):
        """
        Get the balance for a node.
        :param node:
        :return:
        """

        # No root
        if not node:
            return 0

        # Recursively find difference of height of left and right node
        return self.getHeight(node.left) - self.getHeight(node.right)



    def put(self, root, k, v):
        """
        Put a new node into a tree.
        :param root:
        :param k:
        :param v:
        :return:
        """

        # Empty tree
        if not root:
            return AVLTreeNode(k, v)

        # Traverse left down tree to put value
        elif k < root.key:
            root.left = self.put(root.left, k, v)

        # Traverse right down tree to put value
        else:
            root.right = self.put(root.right, k, v)

        # Update root height
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1

        # Get balance factor
        balance_fac = self.getBalance(root)


        # Case 1: LL
        if balance_fac > 1 and k < root.left.key:
            return self.rightRotate(root)
        # Case 2: RR
        if balance_fac < -1 and k > root.right.key:
            return self.leftRotate(root)
        # Case 3: LR
        if balance_fac > 1 and k > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Case 4: RL
        if balance_fac < -1 and k < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, A):
        """
        Perform a left rotation.
        :param A:
        :return:
        """

        B = A.right
        beta = B.left

        # Do rotation
        B.left = A
        A.right = beta

        # Update heights
        A.height = max(self.getHeight(A.left), self.getHeight(A.right)) + 1
        B.height = max(self.getHeight(B.left), self.getHeight(B.right)) + 1

        return B

    def rightRotate(self, B):
        """
        Perform a right rotation
        :param B:
        :return:
        """

        A = B.left
        beta = A.right

        # Do rotation
        A.right = B
        B.left = beta

        # Update heights
        A.height = max(self.getHeight(A.left), self.getHeight(A.right)) + 1
        B.height = max(self.getHeight(B.left), self.getHeight(B.right)) + 1

        return A

if __name__ == "__main__":
    key_val_dict = {15: "bob", 0: "anna", 24: "tom", 10: "david", 13: "david",
                    7: "ben", 30: "karen", 36: "erin", 25: "david", 3: "lucas",}
    my_avl_tree = AVLTreeMap()

    for key, val in key_val_dict.items():
        my_avl_tree.root = my_avl_tree.put(my_avl_tree.root, key, val)
    for key in key_val_dict.keys():
        print(my_avl_tree.get(my_avl_tree.root, key))
