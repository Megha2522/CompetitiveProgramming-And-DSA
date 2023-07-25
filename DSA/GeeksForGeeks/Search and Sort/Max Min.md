# [Max Min](https://practice.geeksforgeeks.org/problems/max-min/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article)
```c++
class Solution
{
   public:
    int findSum(int A[], int N)
    {
    	//code here.
    	int mx = A[0] , mn = A[0];
    	for(int i=1 ; i<N ; i++){
    	    mn = min({mn, A[i]});
    	    mx = max({mx, A[i]});
    	}
    	return mn + mx;
    }

};
```