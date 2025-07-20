# [Connected Components in an Undirected Graph](https://www.geeksforgeeks.org/problems/connected-components-in-an-undirected-graph/1)

```c++

class Solution {
  public:

    void dfs(int v, vector<int>& vis, vector<int>& temp, vector<vector<int>>& ar) {
        vis[v] = 1;            
        temp.push_back(v);     
    
        for (int child : ar[v]) {
            if (vis[child] == 0) {
                dfs(child, vis, temp, ar);
            }
        }
    }

    vector<vector<int>> getComponents(int V, vector<vector<int>>& edges) {
        
        vector<vector<int>> ar(V+1);
        int M = edges.size();
        
        for(int i=0 ; i<M ; i++) {
            int a = edges[i][0] , b = edges[i][1];
            ar[a].push_back(b);
            ar[b].push_back(a);
        }
        
        vector<int> vis(V,0);
        vector<vector<int>> ans;
        
        int cc_count = 0;
        for(int i=0 ; i<V ; i++) {
            if(vis[i] == 0){
                vector<int> temp;
                dfs(i,vis,temp,ar);
                ans.push_back(temp);
            }
        }
        return ans;
    }
};
```