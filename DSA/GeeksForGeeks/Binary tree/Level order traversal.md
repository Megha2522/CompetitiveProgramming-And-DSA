# [Level order traversal](https://www.geeksforgeeks.org/problems/level-order-traversal/1)

```c++
class Solution {
public:
    vector<int> levelOrder(Node* node) {
        queue<Node*> q;
        vector<int> answer;
        
        q.push(node);
        
        while(!q.empty()) {
            int n = q.size();
            for(int i=0;i<n;i++) {
                Node* ptr = q.front(); q.pop();
                answer.push_back(ptr->data);
                
                if(ptr->left != nullptr) q.push(ptr->left);
                if(ptr->right != nullptr) q.push(ptr->right);
            }
        }
        
        return answer;
    }
};

```