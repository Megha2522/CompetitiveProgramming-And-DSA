# [Minimum sum partition](https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1)

## recursion 
```c++
class Solution {

  public:
    int minDifference(vector<int>& arr) {
        
        int n = arr.size();
        int sum = 0;
        for(int i = 0 ; i<n ; i++) {
            sum = sum + arr[i];
        }
        int dp[n+1][sum+1];
        
        int taken , notTaken;
        for(int i = 0 ; i<n+1 ; i++) {
            for(int j = 0 ; j<sum+1 ; j++) {
                if(i == 0) {
                    dp[i][j] = j == 0 ? 1:0;
                    continue;
                }
                if(j == 0) {
                    dp[i][j] = 1;
                    continue;
                }
                taken = 0;
                if(arr[i-1] <= j) {
                    taken = dp[i-1][j-arr[i-1]];
                }
                notTaken = dp[i-1][j];
                dp[i][j] = taken || notTaken;
            }
        }
        int mn = INT_MAX;
        for(int i = 0 ; i<= sum/2 ; i++) {
            if(dp[n][i] == 1)
                mn = min(mn , sum - (2*i));
        }
        return mn ;
    }
};
```

## iteration
```c++
class Solution {

  public:
    int dp[100002][100002];
    int subsetSum(vector<int> arr , int sum , int ind) {
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
    int minDifference(vector<int>& arr) {
        
        int n = arr.size();
        int sum = 0;
        for(int i = 0 ; i<n ; i++) {
            sum = sum + arr[i];
        }
        memset(dp , -1, sizeof(dp));
        subsetSum(arr , sum , n-1);
        int mn = INT_MAX;
        for(int i = 0 ; i<= sum/2 ; i++) {
            if(dp[n][i] == 1)
                mn = min(mn , sum - (2*i));
        }
        return mn ;
    }
};
```