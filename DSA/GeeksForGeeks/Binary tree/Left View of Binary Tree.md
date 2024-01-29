# [Left View of Binary Tree](https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1)

```c++
void PreOrder(Node *root , vector<int>& res , int level) {
    
    if(root == nullptr) return;
    
    if(level >= res.size())
        res.push_back(root->data);
        
    PreOrder(root->left , res , level+1);
    PreOrder(root->right , res , level+1);
    
}
vector<int> leftView(Node *root)
{
   vector<int> res;
   PreOrder(root , res , 0);
   return res;
}

```