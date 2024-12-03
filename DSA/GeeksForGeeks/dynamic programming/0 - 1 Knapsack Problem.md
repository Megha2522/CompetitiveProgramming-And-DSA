# [0 - 1 Knapsack Problem](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)
## recursion
```c++
class Solution
{
    int dp[1000][1000];
    
    int maxProfit(int index , int capacity , int wt[] , int val[]) {
        
        if(index < 0 ) return 0;
        
        if(dp[index][capacity] != -1 ) return dp[index][capacity];
        
        //Take
        int takeProfit = (wt[index] <= capacity) ?
        val[index] + maxProfit(index-1 , capacity - wt[index] , wt , val)
        :0;
            
        //leave
        int leaveProfit = maxProfit(index-1 , capacity , wt , val);
        
        int answer = max(takeProfit , leaveProfit);
        dp[index][capacity] = answer;
        return answer;
    }
    
    public:
    //Function to return max value that can be put in knapsack of capacity W.
    int knapSack(int W, int wt[], int val[], int n) 
    {
        memset(dp , -1 , sizeof dp);
        int P = maxProfit(n-1 , W , wt , val);
        return P;
    }
};
```
## iterative
```c++
class Solution {
  public:
    // Function to return max value that can be put in knapsack of capacity.
    
    int knapSack(int capacity, vector<int> &val, vector<int> &wt) {
        int n = val.size();
        long long int dp[n+1][capacity+1];
        int itemTaken , itemNotTaken;
        
        for(int i =0 ; i<n+1 ; i++) {
            for(int j = 0 ; j<capacity+1 ; j++) {
                if(i == 0 || j ==0) {
                    dp[i][j] = 0;
                    continue;
                }
                itemTaken = 0;
                if( j >= wt[i-1] ) {
                    itemTaken = val[i-1] + dp[i-1][j-wt[i-1]];
                }
                itemNotTaken = dp[i-1][j];
                dp[i][j] = max(itemTaken , itemNotTaken);
            }
        }
        return dp[n][capacity];
    }
};
```