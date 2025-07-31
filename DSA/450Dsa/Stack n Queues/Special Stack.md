# [Special Stack](https://www.geeksforgeeks.org/problems/special-stack/1)

```c++
void push(stack<int>& s, int a) {
    if(isEmpty(s) || s.top()>a){ 
        s.push(a);
    } else {
        int x = s.top(); s.pop();
        s.push(a); s.push(x);
    }
}

bool isFull(stack<int>& s, int n) {
    if(s.size() == n) return true;
    else return false;
}

bool isEmpty(stack<int>& s) {
    return s.empty();
}

int pop(stack<int>& s) {
    int x = s.top(); s.pop();
    return x;
}

int getMin(stack<int>& s) {
    return s.top();
}
```