package am_number_of_connected_components_undirected_graph;

public class Solution {
    public int countComponents(int n, int[][] edges) {
        int[] parents = new int[n];
        int[] rank = new int[n];

        for (int idx = 0; idx < n; idx++) {
            parents[idx] = idx;
            rank[idx] = 1;
        }

        int res = n;
        for (int[] e: edges) {
            int uno = e[0];
            int dos = e[1];

            int unoParent = parents[uno];
            int dosParent = parents[dos];
            if (unoParent == dosParent) continue;

            if (rank[unoParent] >= rank[dosParent]) {
                parents[dos] = unoParent;
                rank[uno] += 1;
            } else {
                parents[uno] = dosParent;
                rank[dos] += 1;
            }
            res -= 1;
        }

        return res;
    }
}
