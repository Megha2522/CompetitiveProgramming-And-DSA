# [Stack Permutations](https://www.geeksforgeeks.org/problems/stack-permutations/1)

## solution 1 - using space
```c++
class Solution {
  public:
    bool checkPerm(vector<int>& a, vector<int>& b) {
        queue<int> q1;
        for (int i = 0; i < a.size(); i++) q1.push(a[i]);
        queue<int> q2;
        for (int i = 0; i < b.size(); i++) q2.push(b[i]);
    
        stack<int> st;
            
        while (!q1.empty()){
            int ele = q1.front();
            q1.pop();
            if (ele == q2.front()) {
                q2.pop();
                while (!st.empty()) {
                    if (st.top() == q2.front()) {
                        st.pop();
                        q2.pop();
                    }
                    else
                        break;
                }
            }
            else st.push(ele);
        }
        bool res = (q1.empty() && st.empty());
        return res;
    }
};
```

## solution 2 - without space

```c++
class Solution {
  public:
    bool checkPerm(vector<int>& a, vector<int>& b) {
    
        stack<int> st;
        int j = 0;
            
        for(int i=0 ; i<a.size() ; i++) {
            st.push(a[i]);
            while(!st.empty() && st.top() == b[j]) {
                st.pop();
                j++;
            }
        }
        return st.empty();
    }
};
```
