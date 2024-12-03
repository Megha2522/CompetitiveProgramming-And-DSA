# [Partition Equal Subset Sum](https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1)

## recursion
```c++
class Solution {
  public:
  int dp[202][40002];
    int subsetSum(vector<int>& arr, int sum, int ind) {
        if(sum == 0) 
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
        dp[ind][sum] = (itemTaken || itemNotTaken);
        return dp[ind][sum];
    }
    
    bool equalPartition(vector<int>& arr) {
        memset(dp,-1,sizeof(dp));
        int sum =0 , target;
        //find target
        for(int i=0 ; i<arr.size() ; i++) {
            sum = sum+arr[i];
        }
        if(sum%2 == 0) target = sum/2;
        else return false;
        
        return subsetSum(arr,target,arr.size()-1);
    }
};
```

## iterative
```c++
class Solution {
  public:
    bool equalPartition(vector<int>& arr) {
        int n = arr.size();
        int sum =0 , target;
        
        //find target
        for(int i=0 ; i<n ; i++) {
            sum = sum+arr[i];
        }
        if(sum%2 == 0) target = sum/2;
        else return false;
        
        bool dp[n+1][target+1];
        bool taken , notTaken;
        
        for(int i = 0 ; i<n+1 ; i++) {
            for(int j = 0 ; j<target+1 ; j++) {
                if(i == 0) {
                    dp[i][j] = false; 
                    continue;
                }
                if(j == 0) {
                    dp[i][j] = true;
                    continue;
                }
                dp[0][0] = true;
                taken = false;
                if(arr[i-1] <= j ) {
                    taken = dp[i-1][j-arr[i-1]];
                }
                notTaken = dp[i-1][j];
                dp[i][j] = taken || notTaken;
            }
        }
        return dp[n][target];
    }
};
```