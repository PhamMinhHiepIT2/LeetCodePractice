# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        raw_tree = in_order(root)
        sorted_tree = raw_tree.sort(reverse=True)

def in_order(root):
    if not root:
        return []
    if root and not root.left and not root.right:
        return [root.val]
    return in_order(root.left) + [root.val] + in_order(root.right)

