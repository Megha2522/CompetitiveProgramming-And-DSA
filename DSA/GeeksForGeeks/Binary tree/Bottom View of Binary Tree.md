# [Bottom View of Binary Tree](https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1)

```c++
# define mpipii map<int,pair<int,int>>
class Solution {
    void PreOrder(Node* root, mpipii & mp,int index , int level) {
        if(root == nullptr) return;
        
        if(mp.find(index) == mp.end() || mp[index].second <= level)
            mp[index] = make_pair(root->data , level);

        PreOrder(root->left , mp , index-1 , level+1);
        PreOrder(root->right , mp , index+1 , level+1);
    }
  public:
    vector <int> bottomView(Node *root) {
        
        vector<int> res;
        mpipii mp;
        
        PreOrder(root , mp, 0 , 0);
        
        mpipii :: iterator it = mp.begin();
        while(it != mp.end()){
            res.push_back((it->second).first);
            it++;
        }
        return res;
    }
};
```