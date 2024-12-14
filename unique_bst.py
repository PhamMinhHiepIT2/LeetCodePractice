
from turtle import st

from sklearn.linear_model import ridge_regression
from torch import le


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(start: int, end: int):
    all_trees = []
    if start > end:
        return []
    if start == end:
        return [start]
    for i in range(start, end+1):
        left = build_tree(start, i-1)
        right = build_tree(i+1, end)
        for l in range(left):
            left_tree = left[i]
            for r in range(right):
                right_tree = right[i]
                tree = TreeNode(i)
                tree.left = left_tree
                tree.right = right_tree
                all_trees.append(pre_order(tree))
    return all_trees


def pre_order(root: TreeNode):
    if not root:
        return []
    if root and not root.left and not root.right:
        return [root.val]


class Solution:
    def numTrees(self, n: int) -> int:
        return len(build_tree(1, n))
