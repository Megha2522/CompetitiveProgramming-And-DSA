# Adjacency List
No. of nodes = N
No. of edges = M

vector<int> ar[N+1];

while(M--) {
    cin >> a >> b;
    ar[a].push_back(b);
    ar[b].push_back(a);
}

# DFS
void dfs(int v) {
    vis[v] = 1;
    cout << v << "->";

    for(int i=0 ; i<ar[v].size() ; i++) {
        int child = ar[v][i];
        if(vis[child] == 0) 
            dfs(child);
    }
}

# Counting number of connected components
int cc_count = 0;
for(int i=1 ; i<=n ; i++) {
    if(vis[i] == 0){
        dfs(i);
        cc_count++;
    }
}