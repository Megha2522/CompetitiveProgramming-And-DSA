# [Sort a stack](https://www.geeksforgeeks.org/problems/sort-a-stack/1)

```c++

void sortedInsert(stack<int> &s, int x) {
    // If stack is empty or the element is greater than the top element, push it
    if (s.empty() || x > s.top()) {
        s.push(x);
        return;
    }

    // Remove the top element and recursively insert the element in the remaining stack
    int temp = s.top();
    s.pop();
    sortedInsert(s, x);

    // Push back the removed element to its original position in the stack
    s.push(temp);
}

void SortedStack::sort() {
    // Base case
    if (s.size() == 1) return; 
    // Remove the top element and recursively sort the remaining stack
    int x = s.top();
    s.pop();
    sort();
    // Insert the removed element back into the stack in a sorted manner
    sortedInsert(s, x);
    return;
}
```