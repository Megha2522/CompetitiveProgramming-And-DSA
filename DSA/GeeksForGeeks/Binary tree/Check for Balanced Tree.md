# [Check for Balanced Tree](https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1)

```c++
class Solution{
    int height(Node *root , bool &balanced) {
        
        if(root == nullptr) return 0;
    
        int h1 = 1 + height(root->left , balanced);
        int h2 = 1 + height(root->right , balanced);
        
        if(abs(h1-h2) > 1)
            balanced = false;
        return max(h1,h2);
    }
    public:
    //Function to check whether a binary tree is balanced or not.
    bool isBalanced(Node *root)
    {
        bool balanced = true;
        height(root , balanced);
        return balanced;
    }
};

```