package aj_gas_station;

public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (getSum(gas) < getSum(cost)) {
            return -1;
        }

        int total = 0;
        int res = 0;
        for (int idx = 0; idx < gas.length; idx ++) {
            total += (gas[idx] - cost[idx]);

            if (total < 0) {
                total = 0;
                res = idx + 1;
            }
        }

        return res;
    }

    int getSum(int[] arr) {
        int total = 0;
        for (int n: arr) {
            total += n;
        }
        return total;
    }
}
