class BalanancedBinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def isbalanced(self, root):
        def dfs(root):

            if not root:
                print(root)
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]


root = BalanancedBinaryTree(3)
root.left = BalanancedBinaryTree(9)
root.right = BalanancedBinaryTree(20)
root.left.left = None
root.left.right = None
root.right.left = BalanancedBinaryTree(15)
root.right.right = BalanancedBinaryTree(7)


s = Solution()

print(s.isbalanced(root))
