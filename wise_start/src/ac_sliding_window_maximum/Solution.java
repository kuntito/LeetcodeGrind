package ac_sliding_window_maximum;

import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> queue = new ArrayDeque<>();

        int left = 0;

        int size = (nums.length - k) + 1;
        int[] res = new int[size];
        for (int right = 0; right < nums.length; right ++) {
            while (!queue.isEmpty() && nums[right] > nums[queue.peekLast()]) {
                queue.removeLast();
            }

            queue.addLast(right);
            if (left > queue.peekFirst()) {
                queue.removeFirst();
            }

            if (right + 1 >= k) {
                int idx = right + 1 - k;
                res[idx] = nums[queue.peekFirst()];
                left += 1;
            }
        }

        return res;
    }
}