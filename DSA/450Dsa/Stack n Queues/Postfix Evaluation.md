# [Postfix Evaluation](https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1)

```c++
class Solution {
  public:
  
    int calculate(int a , int b , string op) {
        if(op == "+") return a+b;
        else if(op == "-") return a-b;
        else if(op == "*") return a*b;
        else return a/b;
    }
    
    int evaluate(vector<string>& arr) {
        
        stack<int> st;
        
        for(int i = 0 ; i<arr.size() ; i++) {
            //push
            if(arr[i] == "+" || arr[i] == "-" || arr[i] == "/" || arr[i] == "*") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                st.push(calculate(a,b,arr[i]));
            }
            //pop
            else {
                st.push(stoi(arr[i]));
            }
        }
        return st.top();
    }
};
```