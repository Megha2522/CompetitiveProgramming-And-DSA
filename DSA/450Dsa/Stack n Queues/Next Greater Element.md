# [Next Greater Element](https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1)

```c++
class Solution {
  public:
    vector<int> nextLargerElement(vector<int>& arr) {
        // code here
        
        stack<int> s;
        
        for(int i=arr.size()-1 ; i>=0 ; i--) {
            
            int a = arr[i]; 
            
            if(s.empty()) {
                arr[i] = -1;
                s.push(a);
            }
            else if(s.top() > arr[i]) {
                arr[i] = s.top();
                s.push(a);
            }
            else {
                s.pop();
                i++;
            }
        }
        return arr;
    }
};
```