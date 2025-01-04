package ao_car_fleet;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        List<Interval> intervals = new ArrayList<>();
        int dim = position.length;
        for (int idx = 0; idx < dim; idx++) {
            int pos = position[idx];
            int sp = speed[idx];
            Interval val = new Interval(
                pos,
                pos + sp,
                sp
            );
            intervals.add(val);
        }

        intervals.sort(
            Comparator.comparingInt(
                (Interval a) -> a.start)
                    .thenComparingInt(a -> a.end)
        );

        List<Integer> sortedPosition = new ArrayList<>();
        List<Integer> sortedSpeed = new ArrayList<>();

        for (int idx = 0; idx < dim; idx++) {
            sortedPosition.add(intervals.get(idx).start);
            sortedSpeed.add(intervals.get(idx).speed);
        }

        System.out.println(sortedPosition);
        System.out.println(sortedSpeed);

        return 0;
    }

    class Interval {
        int start;
        int end;
        int speed;

        Interval(int start, int end, int speed) {
            this.start = start;
            this.end = end;
            this.speed = speed;
        }
    }
}

