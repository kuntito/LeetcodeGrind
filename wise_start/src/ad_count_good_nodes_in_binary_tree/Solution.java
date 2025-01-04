package ad_count_good_nodes_in_binary_tree;


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int goodNodes(TreeNode root) {
        if (root == null) return 0;

        int xander = root.val;
        return explore(root, xander);
    }

    int explore(TreeNode node, int xander){
        xander = Math.max(xander, node.val);
        int count = node.val >= xander ? 1: 0;
        if (node.left != null) {
            count += this.explore(node.left, xander);
        }
        if (node.right != null) {
            count += this.explore(node.right, xander);
        }

        return count;
    }
}