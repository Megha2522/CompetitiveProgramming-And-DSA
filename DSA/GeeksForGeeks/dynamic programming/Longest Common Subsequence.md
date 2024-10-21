# [Longest Common Subsequence](https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1)
## recursion
```c++
class Solution {
    int dp[1000][1000];
    
    // Function to find the length of longest common subsequence in two strings.
    int fun(int ia, int ib, string& a, string& b) {
        //base condition
        if(ia < 0 || ib < 0) {
            return 0;
        }
        if(dp[ia][ib] != -1) {
            return dp[ia][ib];
        }
        int res;
        if(a[ia] == b[ib]) {
            res = 1 + fun(ia - 1 , ib - 1 , a , b);
        } else {
            int left = fun(ia - 1, ib ,a, b);
            int right = fun(ia , ib - 1 , a , b);
            res = max(left,right);
        }
        dp[ia][ib] = res;
        return res;
    }
public:
    int lcs(int n, int m, string str1, string str2) {
        memset(dp , -1 , sizeof(dp));
        return fun(n - 1, m - 1, str1, str2);
    }
};

```
## iterative
```c++
class Solution {
  public:
    // Function to find the length of longest common subsequence in two strings.
    int dp[1000][1000];
    int lcs(int n, int m, string str1, string str2) {
        
        int res;
        for(int i=0 ; i<=n ; i++) {
            for(int j=0 ; j<=m ; j++) {
                if(i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else {
                    if(str1[i-1] == str2[j-1]) {
                        dp[i][j] = 1 + dp[i-1][j-1];
                    } else {
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                    }
                }
            }
        }
        return dp[n][m];
    }
};
```
