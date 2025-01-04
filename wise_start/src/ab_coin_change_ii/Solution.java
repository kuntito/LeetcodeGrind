package ab_coin_change_ii;

public class Solution {
    public int change(int amount, int[] coins) {
        int[][] memo = new int[coins.length][amount+1];
        for (int i = 0; i < coins.length; i++) {
            for (int j = 0; j <= amount; j++) {
                memo[i][j] = -1;
            }
        }
        explore(amount, 0, coins, memo);
        return memo[0][amount];
    }

    public int explore(int amount, int idx, int[] coins, int[][] memo) {
        if (idx == coins.length || amount < 0) {
            return 0;
        }
        if (memo[idx][amount] != -1) {
            return memo[idx][amount];
        }
        if (amount == 0) {
            memo[idx][amount] = 1;
            return memo[idx][amount];
        }

        int count = explore(amount, idx + 1, coins, memo);

        int newAmount = amount - coins[idx];
        if (newAmount >= 0) {
            if (newAmount == 0) {
                count += 1;
            } else {
                count += explore(newAmount, idx, coins, memo);
            }
        }

        memo[idx][amount] = count;
        return memo[idx][amount];
    }
}
