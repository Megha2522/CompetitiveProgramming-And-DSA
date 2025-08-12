# [Valid Substring](https://www.geeksforgeeks.org/problems/valid-substring0624/1)

## Sol - 1 using stack

```c++
class Solution {
  public:
    int maxLen(string& s) {
        stack<int> st; st.push(-1);
        int answer = 0;
        
        for(int i=0; i<s.size() ;i++){
            if(s[i]=='(') st.push(i);
            else{
                st.pop();
                if(st.empty()) st.push(i);
                else answer = max(answer, i-st.top());
            }
        }
        
        return answer;
    }
};
```

## Sol - 2 using pointers

```c++
class Solution2 {
  public:
    int findMaxLen(string s) {
        int l = 0, r = 0, n = s.size(), answer = 0;
        
        for(int i=0;i<n;i++){
            if(s[i]=='(') l++;
            else r++;
            if(l==r) answer = max(answer,2*l);
            else if(r>l) l=r=0; //invalid
        }
        
        l = r = 0;
        for(int i=n-1;i>=0;i--){
            if(s[i]=='(') l++;
            else r++;
            if(l==r) answer=max(answer,2*l);
            else if(l>r) l=r=0;
        }
        
        return answer;
    }
};
```