from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.p = ""
        self.paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return dfs(root, self.p, self.paths)


def dfs(root: Optional[TreeNode], p, res):
    if not root.left and not root.right:
        p += str(root.val)
        res.append(p)

    p += str(root.val) + "->"

    if root.left:
        dfs(root.left, p, res)
    if root.right:
        dfs(root.right, p, res)
    return res
