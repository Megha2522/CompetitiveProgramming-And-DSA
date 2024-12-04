# [Perfect Sum Problem](https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1)

## recursive
```c++
class Solution {
  public:
    int dp[1001][1001];
    int subsetSum(vector<int>& arr, int sum, int ind) {
        if(sum == 0 && (ind == -1 || arr[ind] != 0)) 
            return 1;
        if(ind == -1) 
            return 0;
        if(dp[ind][sum] != -1 ) 
            return dp[ind][sum];
            
        int itemTaken = 0 , itemNotTaken;
        
        if(arr[ind] <= sum) {
            itemTaken = subsetSum(arr , sum - arr[ind] , ind-1);
        }
        itemNotTaken = subsetSum(arr , sum , ind-1);
        dp[ind][sum] = (itemTaken + itemNotTaken);
        return dp[ind][sum];
    }
    
    int perfectSum(vector<int>& arr, int target) {
        sort(arr.begin() , arr.end() , greater<int>());
        memset(dp,-1,sizeof(dp));
        return subsetSum(arr,target,arr.size()-1);
    }
};
```

## iterative
```c++
class Solution {
  public:
    int perfectSum(vector<int>& arr, int target) {
        int dp[arr.size()+1][target+1];
        int taken , notTaken;
        sort(arr.begin() , arr.end() , greater<int>());
        
        for(int i=0 ; i<arr.size()+1 ; i++) {
            for(int j = 0 ; j<target+1 ; j++) {
                
                if(i == 0) {
                    dp[i][j] = 0;
                    continue;
                }
                dp[0][0] = 1;
                taken = 0;
                if(arr[i-1] <= j) {
                    taken = dp[i-1][j-arr[i-1]];
                }
                notTaken = dp[i-1][j];
                dp[i][j] = taken + notTaken;
            }
        }
        return dp[arr.size()][target];
    }
};
```