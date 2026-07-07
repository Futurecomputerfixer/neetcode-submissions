class Solution {
    public boolean validTree(int n, int[][] edges) {
        int[] parents = new int[n];
        for(int i = 0; i < n; i++)
            parents[i] = i;
        
        for(int[] edge : edges)
            if(find(edge[0], parents) == find(edge[1], parents))
                return false;
            else parents[find(edge[0], parents)] = find(edge[1], parents);

        boolean connected = false;
        for(int i = 0; i < n; i++)
            if(parents[i] == i)
                if(connected) return false;
                else connected = true;
        
        return true;
            
    }

    public int find(int child, int[] parents){
        if(parents[child] == child)
            return child;
        return find(parents[child], parents);
    }
}
