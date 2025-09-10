package Lab07.pack;

public class GridPaths {
    public int numberOfPaths(int[][] grid) {
        return findNumberOfPaths(grid, 0, 0);
    }

    private int findNumberOfPaths(int[][] grid, int row, int col) {
        if (row == grid.length - 1 && col == grid[0].length - 1) {
            return 1;
        } else {
            if (grid[row][col] == 1) return 0;
            if (row == grid.length - 1) return findNumberOfPaths(grid, row, col + 1);
            if (col == grid[0].length - 1) return findNumberOfPaths(grid, row + 1, col);
            return findNumberOfPaths(grid, row + 1, col) + findNumberOfPaths(grid, row, col + 1);
        }
    }
}
