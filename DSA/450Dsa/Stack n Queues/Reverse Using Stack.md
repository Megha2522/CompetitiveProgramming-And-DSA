# [Reverse Using Stack](https://www.geeksforgeeks.org/problems/reverse-a-string-using-stack/1)

```c++
class Solution {
  public:
    string reverse(const string& S) {
        stack<char> st;
        
        for (auto c : S)
            st.push(c);
        
        string res;
        while (!st.empty()) {
            res += st.top();
            st.pop();
        }
        return res;
    }
};
```