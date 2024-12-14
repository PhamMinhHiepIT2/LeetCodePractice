from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = dfs(root, [], "")
        print(res)
        return res


def dfs(root: TreeNode, res, p):
    if root and not root.left and not root.right:
        p += str(root.val)
        res.append(p)
        p = ""
    else:
        dfs(root.left, res, p)
        dfs(root.right, res, p)
    return res
