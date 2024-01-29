# [Top View of Binary Tree](https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1)

## Solution 1: c++ - DFS and hashMap

```c++
#define mpipii map<int,pair<int,int>> 
class Solution
{
    public:
    void PreOrder(Node* root, mpipii & mp , int index , int level) {
        if(root == nullptr) return;
        
        if(mp.find(index) == mp.end() || mp[index].second > level)
            mp[index] = make_pair(root->data,level);
            
        PreOrder(root->left , mp , index-1 , level+1);
        PreOrder(root->right , mp , index+1 , level+1);
        
    }
    vector<int> topView(Node *root)
    {
        vector<int> res;
        mpipii mp;
        
        PreOrder(root , mp , 0 , 0);
        
        mpipii ::iterator it = mp.begin();
        while(it != mp.end()) {
            res.push_back((it->second).first);
            it++;
        }
        return res;
    }
}
```