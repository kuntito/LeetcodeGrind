import ap_validate_bst.Solution;
import ap_validate_bst.TreeNode;

import java.util.Arrays;

public class Main {
    public static void main(String[] args){
//        int[] hand = new int[] {1,2,3,6,2,3,4,7,8};
//        int groupSize = 3;

//        int[] hand = new int[] {9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11};
//        int groupSize = 10;

//        var three = new TreeNode(3);
//        var one = new TreeNode(1);
//        var zero = new TreeNode(0);
//        var two = new TreeNode(2);
//        var three2 = new TreeNode(3);
//        var five = new TreeNode(5);
//        var four = new TreeNode(4);
//        var six = new TreeNode(6);
//
//
//        five.left = four;
//        five.right = six;
//        three.right = five;
//
//        three.left = one;
//        one.left = zero;
//        one.right = two;
//        two.right = three2;

        var a = new TreeNode(-2147483648);
        var b = new TreeNode(2147483647);
        var c = new TreeNode(-2147483648);

        a.right = b;
        b.left = c;

        var sol = new Solution();
        var res = sol.isValidBST(a);
        System.out.println(res);
    }
}