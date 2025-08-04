# [The Celebrity Problem](https://www.geeksforgeeks.org/problems/the-celebrity-problem/1)

```c++
class Solution {
  public:
    int celebrity(vector<vector<int> >& mat) {
        int ans = -1;
        for(int i = 0 ; i<mat.size() ; i++) {
            int sum = 0;
            for(int j = 0 ; j<mat[0].size() ; j++) {
                sum += mat[i][j];
            }
            if(sum == 1) {
                ans = i;
                break;
            }
        }
        for(int k = 0 ; k<mat.size() ; k++) {
            if(mat[k][ans] == 0) ans = -1;
        }
        return ans;
    }
};
```