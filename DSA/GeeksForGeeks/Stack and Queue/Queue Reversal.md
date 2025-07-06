# [Queue Reversal](https://www.geeksforgeeks.org/problems/queue-reversal/1)

## recursion
```c++

class Solution {
  public:
  
    void reverse(queue<int> &q) {
        if(q.empty()) return;
        
        int ele = q.front();
        q.pop();
        reverse(q);
        q.push(ele);
    }
    
    queue<int> reverseQueue(queue<int> &q) {
        
        reverse(q);
        return q;
    }
};
```

## using stack
```c++

class Solution {
  public:
    queue<int> reverseQueue(queue<int> &q) {
        
        stack<int> s;
        
        while(!q.empty()) {
            int a = q.front();
            q.pop();
            s.push(a);
        }
        while(!s.empty()) {
            q.push(s.top());
            s.pop();
        }
        return q;
    }
};
```