package ap_validate_bst;

import com.sun.source.tree.Tree;

public class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;

        long abyss = -2147483648L - 1;
        long skypiea = 2147483647L + 1;
        return explore(root, abyss, skypiea);
    }

    boolean explore(
        TreeNode node,
        long minimum,
        long maximum
    ) {
        if (node == null) return true;
        if ((node.val <= minimum) || (node.val >= maximum)) return false;

        return explore(
            node.left,
            minimum,
            node.val
        ) && explore(
            node.right,
            node.val,
            maximum
        );
    }
}