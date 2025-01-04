package ak_coin_change;

//https://leetcode.com/problems/coin-change/
import java.util.Arrays;

public class Solution {
    public int coinChange(int[] coins, int amount) {
        int lastIndex = coins.length - 1;
        Arrays.sort(coins);

        explore(lastIndex, coins, amount, 0);

        return 0;
    }

    int explore(int idx, int[] coins, int amount, int count) {
        if (amount == 0) {
            return count;
        }

        int c = coins[idx];
        int newAmount = amount - c;
        if (newAmount >= 0) {
            explore(idx, coins, newAmount, count + 1);
        } else {
            explore(idx-1, coins, newAmount, count + 1);
        }

        return 0;
    }
}
