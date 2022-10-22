from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.p = ""
        self.cur_p = ""
        self.paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left is None and root.right is None:
            print("Current root: {}".format(root))
            self.p += str(root.val)
            self.paths.append(self.p)
            print("Current p: {}".format(self.p))
            self.p = ""
            return list(set(self.paths))

        elif root.left != None and root.right == None:
            print("Go to left leaf")
            print("Current root: {}".format(root))
            self.p += (str(root.val) + "->")
            self.binaryTreePaths(root.left)
            print("Current p: {}".format(self.p))
        elif root.left == None and root.right != None:
            print("Go to right leaf")
            print("Current root: {}".format(root))
            self.p += (str(root.val) + "->")
            self.binaryTreePaths(root.right)
            print("Current p: {}".format(self.p))
        else:
            self.cur_p = self.p
            self.p = ""
            left_res = self.binaryTreePaths(root.left)
            print("Left res: {}".format(left_res))
            right_res = self.binaryTreePaths(root.right)
            print("Right res: {}".format(right_res))
            self.paths = merge_2_side(
                left_res, right_res, root.val, self.cur_p)
            return list(set(self.paths))
        # return list(set(self.paths))


def merge_2_side(left_res: list, right_res: list, root: int, p: str):
    print("Merging {} and {}".format(left_res, right_res))
    res = left_res + right_res
    new_res = []
    for el in res:
        new_el = str(root) + "->" + el
        # new_el = p + new_el
        new_res.append(new_el)
    return new_res
