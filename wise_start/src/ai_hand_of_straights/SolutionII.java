package ai_hand_of_straights;

import java.util.*;

public class SolutionII {

    public boolean isNStraightHand(int[] hand, int groupSize) {
        if ((hand.length % groupSize) > 0) return false;
        HashMap<Integer, Pair> map = new HashMap<>();
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int n: hand) {
            if (map.containsKey(n)) {
                map.get(n).count++;
            } else {
                Pair pair = new Pair(n, 1);
                map.put(n, pair);
                minHeap.add(n);
            }
        }

        while (map.size() >= groupSize) {
            while (!map.containsKey(minHeap.peek())) {
                minHeap.remove();
            }
            int item = minHeap.peek();

            for (int i = 0; i < groupSize; i++){
                if (!map.containsKey(item)) return false;
                Pair pair = map.get(item);
                pair.count--;
                if (pair.count == 0) {
                    map.remove(item);
                }

                item++;
            }
        }

        return map.isEmpty();
    }
}
