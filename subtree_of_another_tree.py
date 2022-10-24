from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        len_tree = 0
        len_subtree = 0
        if calc_tree_len(root, len_tree) == 1 and calc_tree_len(subRoot, len_subtree) == 1 and root.val != subRoot.val:
            return False
        subtree = ""
        tree = ""
        read_sub_tree = read_tree(subRoot, subtree)
        read_tree = read_tree(root, tree)
        return read_sub_tree in read_tree


def read_tree(tree: TreeNode, res):

    if tree is None:
        return "+"
    else:
        res += str(tree.val) + str(read_tree(tree.left)) + \
            str(read_tree(tree.right))
    return res


def calc_tree_len(tree, len_tree):

    if tree is None:
        return 0
    else:
        len_tree += calc_tree_len(tree.left, len_tree) + \
            calc_tree_len(tree.right, len_tree)
        return len
