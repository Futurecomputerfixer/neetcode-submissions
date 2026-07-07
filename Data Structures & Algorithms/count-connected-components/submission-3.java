class Solution {
    public int countComponents(int n, int[][] edges) {
        int[] parents = new int[n];
        for(int i = 0; i < n; i++)
            parents[i] = i;
        for(int[] edge : edges)
        {
            if(find(parents, edge[0]) != find(parents, edge[1]))
            parents[find(parents, edge[0])] = find(parents, edge[1]);
        }
        int cnt = 0;
        for(int i = 0; i < n; i++)
            if(parents[i] == i) cnt++;
        
        return cnt;
    }

    public int find(int[] parents, int child){
        if(parents[child] == child)
            return child;
        return find(parents, parents[child]);
    }
}
