# [Sum Tree](https://www.geeksforgeeks.org/problems/sum-tree/1)

```c++
class Solution
{
    int sum(Node* root) {
        
        if(root == nullptr) return 0;
        
        int left = sum(root->left);
        int right = sum(root->right);
        
        if(left + right == root->data || (left == 0 && right == 0))
            return left+right+root->data;
        else
            return INT_MIN;
            
    }
    public:
    bool isSumTree(Node* root)
    {
        if(root == nullptr) return true;
        
        int ans = sum(root);
        
        if(ans < 0) return false;
        else return true;
    }
};
```