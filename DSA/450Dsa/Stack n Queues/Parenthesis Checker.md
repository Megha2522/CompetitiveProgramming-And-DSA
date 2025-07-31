# [Parenthesis Checker](https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1)

## using stack

```c++
class Solution {
  public:
    bool isBalanced(string& k) {
        // code here
        stack<char> st;
        for(int i = 0; i < k.length(); i++) {
            if(k[i] == '(' || k[i] == '{' || k[i] == '[') 
                st.push(k[i]);
            else {
                if (!st.empty()) {
                    if ((st.top() == '(' && k[i] == ')') || (st.top() == '{' && k[i] == '}') || (st.top() == '[' && k[i] == ']'))
                        st.pop();
                    else return false;
                } else return false;
            }
        }
        return st.empty(); // If stack is empty, return true (balanced), otherwise false
    }
};
```

## without using stack

```c++

class Solution {
  public:
  
    bool checkMatch(char c1, char c2){
        if (c1 == '(' && c2 == ')') return true;
        if (c1 == '[' && c2 == ']') return true;
        if (c1 == '{' && c2 == '}') return true;
        return false;
    }
    
    bool isBalanced(string& k) {
        int top = -1;
        for (int i = 0; i < k.length(); ++i){
          
            // Push char if stack is empty or no match
            if (top < 0 || checkMatch(k[top], k[i]) == false){
                ++top;
                k[top] = k[i];
            }
            else {
                // Pop from stack if match found
                --top;
            }
        }
        // Return true if stack is empty (balanced)
        return top == -1;
    }
};
```