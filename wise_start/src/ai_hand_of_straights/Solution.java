package ai_hand_of_straights;

import java.util.*;

public class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if ((hand.length % groupSize) > 0) return false;
        HashMap<Integer, Pair> map = new HashMap<>();
        List<Integer> lst = new ArrayList<>();

        for (int n: hand) {
            if (map.containsKey(n)) {
                map.get(n).count++;
            } else {
                Pair pair = new Pair(n, 1);
                map.put(n, pair);
                lst.add(n);
            }
        }

        lst.sort(Comparator.comparingInt(a -> a));

        int idx = 0;
        while (map.size() >= groupSize) {
            int item = -1;
            while (idx < lst.size()) {
                int n = lst.get(idx);
                if (map.containsKey(n)){
                    item = n;
                    break;
                }
                idx++;
            }

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

class Pair {
    int number;
    int count;

    public Pair(int number, int count) {
        this.number = number;
        this.count = count;
    }
}
