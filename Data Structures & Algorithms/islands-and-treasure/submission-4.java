class Solution {
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int m = grid.length, n = grid[0].length;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(grid[i][j] == 0)
                    q.add(new int[] {i, j});

        if(q.size() == 0) return;
        
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while(!q.isEmpty()){
            int[] index = q.poll();
            int row = index[0];
            int col = index[1];
            for(int[] dir : dirs){
                int x = row + dir[0];
                int y = col + dir[1];
                if(x < 0 || y < 0 || x >= m || y >= n || grid[x][y] != Integer.MAX_VALUE)
                    continue;
                grid[x][y] = grid[row][col] + 1;
                q.add(new int[] {x, y});
            }
        }
    }
}
