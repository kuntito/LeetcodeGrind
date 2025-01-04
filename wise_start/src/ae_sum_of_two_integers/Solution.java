package ae_sum_of_two_integers;

public class Solution {
    public int getSum(int a, int b) {
        // bit  - XOR then XOR
        // carry - AND then OR

        int carry = 0;
        int shift = 0;

        int res = 0;
        while (a > 0 || b > 0) {
            int bitOne = a & 1;
            int bitTwo = b & 1;

            int bit = (bitOne ^ bitTwo) ^ carry;
            carry = (bitOne & bitTwo) | carry;

            for (int i = 0; i < shift; i++) {
                bit <<= 1;
            }

            res |= bit;

            a >>= 1;
            b >>= 1;
            shift += 1;
        }

        for (int i = 0; i < shift; i++) {
            carry <<= 1;
        }

        res |= carry;

        return res;
    }
}