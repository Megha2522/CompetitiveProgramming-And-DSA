# [Value equal to index value](https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1)
```c++
class Solution{
public:

	vector<int> valueEqualToIndex(int arr[], int n) {
	    // code here
	    vector<int> ans;
	    int index = 0; 
	    for(int i = 1 ; i <= n ; i++){
	        if(arr[index] == i)
	        ans.push_back(arr[index]);
	        index++;
	    }
	    return ans;
	}
};
```