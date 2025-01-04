package ag_set_matrix_zeroes;

import java.util.Arrays;

public class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        boolean doFirstRow = false;
        for (int val: matrix[0]) {
            if (val == 0) {
                doFirstRow = true;
                break;
            }
        }

        for (int ri = 1; ri < rows; ri++) {
            for (int ci = 1; ci < cols; ci++) {
                int val = matrix[ri][ci];
                if (val == 0) {
                    matrix[0][ci] = 0;
                    matrix[ri][0] = 0;
                }
            }
        }

//        for (int[] row: matrix) {
//            System.out.println(Arrays.toString(row));
//        }


        for (int ci = 0; ci < cols; ci++) {
            if (matrix[0][ci] == 0) {
                for (int ri = 1; ri < rows; ri++) {
                    matrix[ri][ci] = 0;
                }
            }
        }

        for (int ri = 1; ri < rows; ri++){
            if (matrix[ri][0] == 0) {
                for (int ci = 1; ci < cols; ci++) {
                    matrix[ri][ci] = 0;
                }
            }
        }

        if (doFirstRow) {
            for (int ci = 0; ci < cols; ci++) {
                matrix[0][ci] = 0;
            }
        }
    }
}