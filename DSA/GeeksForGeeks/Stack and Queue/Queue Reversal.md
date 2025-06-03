# [Queue Reversal](https://www.geeksforgeeks.org/problems/queue-reversal/1)

## recursion
```c++
// function Template for C++

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