package ah_pow;

public class Solution {
    public double myPow(double x, int n) {
        if (x == 0) return 0;
        if (x == 1) return 1;

        int foo = Math.abs(n);
        boolean isOdd = foo % 2 == 1;
        if (isOdd) {
            foo -= 1;
        }

        double res = explore(x, foo);
        if (isOdd) {
            res *= x;
        }

        return n > 0 ? res : 1/res;
    }

    double explore(double x, int n) {
        if (n == 2){
            return x * x;
        }

        return explore(x, n/2) * explore(x, n/2);
    }
}
