# [Diameter of a Binary Tree](https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1)

```c++
class Solution {
    int answer;
    int height(Node* root) {
        if(root == nullptr)
            return 0;
            
        int left = height(root->left);
        int right = height(root->right);
        
        answer = max(answer, left + right + 1);
        
        return  max(left,right) + 1;
    }
public:
    // Function to return the diameter of a Binary Tree.
    int diameter(Node* root) {
        answer = 0;
        height(root);
        return answer;
    }
};
```