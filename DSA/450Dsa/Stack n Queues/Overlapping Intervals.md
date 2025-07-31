# [Overlapping Intervals](https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1)

```c++
class Solution {
  public:
    static bool compare(vector<int> &a , vector<int> &b) {
        return a[0] < b[0];
    }
    vector<vector<int>> mergeOverlap(vector<vector<int>>& arr) {
        
        sort(arr.begin() , arr.end() , compare);

        vector<vector<int>> res;
        vector<int> inter;

        inter.push_back(arr[0][0]);
        inter.push_back(arr[0][1]);

        for(int i = 1 ; i < arr.size() ; i++) {
            if(arr[i][0] <= inter[1]) {
                if(arr[i][1] > inter[1]) {
                    inter[1] = arr[i][1];
                }
            } else {
                res.push_back(inter);
                inter[0] = arr[i][0];
                inter[1] = arr[i][1];
            }
        }
        res.push_back(inter);
        return res;
        
    }
};
```