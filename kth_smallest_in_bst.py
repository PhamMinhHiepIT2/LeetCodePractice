from typing import Optional
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = in_order(root)
        heapq.heapify(tree)
        ans = -1
        while k > 0:
            ans = heapq.heappop(ans)
        return ans


def in_order(root: Optional[TreeNode]):
    if not root:
        return []
    if root and not root.left and not root.right:
        return [root.val]
    return in_order(root.left) + [root.val] + in_order(root.right)
