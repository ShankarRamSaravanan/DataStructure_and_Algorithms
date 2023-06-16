class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_data(self, data):
        if data == self.data:  # This checks whether the element is already there in the tree
            return

        # If the data is lesser than the root node(self.data) then create a node and add it to the left side
        if data < self.data:

            if self.left:  # If an element exist in the left node there comes the recursion where you check
                self.left.add_data(data)
            else:
                self.left = BinaryTreeNode(data)

        if data > self.data:

            if self.right:
                self.right.add_data(data)
            else:
                self.right = BinaryTreeNode(data)

    def inorder_Traversal(self):

        element = []

        # First visit left node take all the elements
        if self.left:
            element += self.left.inorder_Traversal()

        # Then Vist base node
        element.append(self.data)

        if self.right:
            element += self.right.inorder_Traversal()

        return element

    def val_exist(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.val_exist(val)
            else:
                return False

        if val > self.data:
            if self.right:
                print(self.right.data)
                return self.right.val_exist(val)
            else:
                return False

    def find_max(self):

        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):

        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    # def delete(self):


def build_tree(element):

    root = BinaryTreeNode(element[0])

    for i in range(1, len(element)):
        root.add_data(element[i])
    return root


numbers = [1, 2, 98, 12, 1222, 44, 1224, 5663, 1913, 3, 2, 44, 67, 43, 91]
numberss = build_tree(numbers)
print(numberss.inorder_Traversal())
print(numberss.val_exist(1222))

print(numberss.find_max())
