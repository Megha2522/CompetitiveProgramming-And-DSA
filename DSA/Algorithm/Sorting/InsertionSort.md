# Insertion Sort

- Time Complexity:
    - Best Case: O(1)
    - Worst Case: O(n^2) = O(n) x O(n) x O(1)

- Space Complexity: O(1) 

```c++
for (int i = 1; i < n; i++) {
    int element = a[i];
    int j = i - 1;
    while (j >= 0 && a[j] > element) {
        a[j + 1] = a[j];
        j--;
    }
    a[j + 1] = element;
}
```
