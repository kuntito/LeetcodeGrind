package af_swim_in_rising_water;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;


public class Solution {
    public int swimInWater(int[][] grid) {
        PriorityQueue<Pair> minHeap = new PriorityQueue<>((a,b) -> a.distance - b.distance);

        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        HashMap<Position, Position> prevMap = new HashMap<>();

        Pair lastNode = explore(grid, visited, minHeap, prevMap);
        System.out.println(lastNode);

        return 0;
    }

    Pair explore(
        int[][] grid,
        boolean[][] visited,
        PriorityQueue<Pair> minHeap,
        HashMap<Position, Position> prevMap
    ) {
        int rows = grid.length;
        int cols = grid[0].length;

        Pair curr = new Pair(0, new Position(0, 0));
        minHeap.add(curr);
        prevMap.put(curr.pos, curr.pos);

        while (true) {
            Pair node = minHeap.remove();
            if (node.pos.ri == rows - 1 && node.pos.ci == cols) {
                return node;
            }
            if (visited[node.pos.ri][node.pos.ci]) {
                continue;
            }
            visited[node.pos.ri][node.pos.ci] = true;

            for (Position nei: getNeighbours(node.pos, visited)) {
                Pair newPair = new Pair(
                    node.distance + grid[nei.ri][nei.ci],
                    nei,
                    node
                );
                minHeap.add(newPair);
            }
        }
    }

    List<Position> getNeighbours(Position origin, boolean[][] visited) {
        int rows = visited.length;
        int cols = visited[0].length;

        int ri = origin.ri;
        int ci = origin.ci;

        Position[] foo = new Position[] {
            new Position(ri - 1, ci),
            new Position(ri + 1, ci),
            new Position(ri, ci - 1),
            new Position(ri, ci + 1),
        };

        List<Position> validPositions = new ArrayList<>();
        for (Position pos : foo) {
            if (pos.ri >= 0 && pos.ri < rows && pos.ci >= 0 && pos.ci < cols && !visited[pos.ri][pos.ci]) {
                validPositions.add(pos);
            }
        }
        return validPositions;
    }
}

class Pair {
    int distance;
    Position pos;
    Pair prev;

    Pair (int distance, Position pos) {
        this.distance = distance;
        this.pos = pos;

        new Pair(distance, pos, null);
    }

    Pair (int distance, Position pos, Pair prev) {
        this.distance = distance;
        this.pos = pos;
        this.prev = prev;
    }

    @Override
    public String toString() {
        return this.pos + " from " + this.prev;
    }
}

class Position {
    int ri;
    int ci;
    Position(int ri, int ci) {
        this.ri = ri;
        this.ci = ci;
    }

    @Override
    public String toString() {
        return "(" + this.ri + "," + this.ci + ")";
    }
}