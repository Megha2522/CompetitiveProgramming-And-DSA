# [Height of Binary Tree](https://www.geeksforgeeks.org/problems/height-of-binary-tree/1)

## Solution 1:  C++ - Level order traversal (BFS)

```c++
// Time Complexity: O(N)
// Auxiliary Space: O(N)

class Solution {
    public:
    //Function to find the height of a binary tree.
    int height(struct Node* node){
        queue<Node* > q;
        q.push(node);
        
        if (node == NULL)
            return 0;
            
        int count = 0;
        while(!q.empty()){
            count++;
            int s = q.size();
            for(int i=0 ; i<s ; i++){
                
                Node* ptr = q.front(); q.pop();
                
                if(ptr->left != NULL) q.push(ptr->left);
                if(ptr->right != NULL) q.push(ptr->right);
                
            }
        }
        return count;
    }
};
```

## Solution 2 - Inorder traversal (DFS)
```c++
// Time Complexity: O(N)
// Auxiliary Space: O(N)

class Solution{
public:
    int height(struct Node* node){
        // node is null
        if(node == nullptr)
            return 0;
        
        int left = height(node->left);
        int right = height(node->right);
        
        return 1 + max(left,right);
    }
};
```