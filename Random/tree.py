class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_data(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_data()

    def invertTree(self):

        if not self.data:
            return None
        tmp = self.left
        self.left = root.right
        self.right = tmp

        self.invertTree(self.left)

        self.invertTree(self.right)

        return root


def buil_tree():

    root = TreeNode(4)

    first_child = TreeNode(2)
    first_child.add_child(TreeNode(1))
    first_child.add_child(TreeNode(3))

    s_child = TreeNode(7)
    s_child.add_child(TreeNode(6))
    s_child.add_child(TreeNode(9))

    root.add_child(first_child)
    root.add_child(s_child)

    # root = TreeNode("Electronics")
    # cellphone = TreeNode("Cellphone")
    # cellphone.add_child(TreeNode("Motorola"))
    # cellphone.add_child(TreeNode("Samsung"))

    # Laptop = TreeNode("Laptop")
    # Laptop.add_child(TreeNode("Mac"))
    # Laptop.add_child(TreeNode("Hp"))

    # root.add_child(Laptop)
    # root.add_child(cellphone)

    return root


root = buil_tree()

root.print_data()


