# Bubble Sort

-Time Complexity:
    - Best Case: O(1)
    - Worst Case: O(n^2) = O(n) x O(n) x O(1)

- Space Complexity: O(1)

```c++
for(int i=0 ; i<n-1 ; i++){ // No. of passes
  bool isSorted = true;
  for(int j=0 ; j<n-i-1 ; j++){ // No. of steps in each pass
    if(arr[j] > arr[j+1]){
      int temp = arr[j];
      arr[j] = arr[j+1];
      arr[j+1] = temp;
      isSorted = false;
    }
    if(isSorted)  break;
  }
}
```