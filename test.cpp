class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if(root &&  !root.left && !root.right && root.val == 0) {
            root = NULL
        }
    }
};