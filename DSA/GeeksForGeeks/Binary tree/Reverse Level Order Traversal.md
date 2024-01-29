# [Reverse Level Order Traversal](https://www.geeksforgeeks.org/problems/reverse-level-order-traversal/1)

## Solution 1: C++ - Level Order Traversal
```c++
vector<int> reverseLevelOrder(Node *root) {
    queue<Node *> q;
    vector<int> ans;
    
    q.push(root);
    
    while(! q.empty()){
       
        int len = q.size();

        for(int i=0 ; i<len ; i++){
            
            Node* node = q.front(); 
            ans.push_back(node->data);
            q.pop();
            
            if(node->right != nullptr) q.push(node->right);
            if(node->left != nullptr) q.push(node->left);
           
        }
    }
    reverse(ans.begin(), ans.end());
    
    return ans;
}
```