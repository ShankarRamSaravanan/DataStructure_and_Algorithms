# Python3 program to convert a binary
# tree to its mirror

# Utility function to create a new
# tree de


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def mirror(self, node):

        if (node == None):
            return
        else:

            temp = node

            """ do the subtrees """
            self.mirror(node.left)
            self.mirror(node.right)

            """ swap the pointers in this node """
            temp = node.left
            node.left = node.right
            node.right = temp

    def inOrder(self, node):
        print(node)
        if (node == None):
            return

        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

print("Inorder traversal of the",
      "constructed tree is")
root.inOrder(root)

""" Convert tree to its mirror """
root.mirror(root)

""" Print inorder traversal of
    the mirror tree """
print("\nInorder traversal of",
      "the mirror tree is ")
root.inOrder(root)
