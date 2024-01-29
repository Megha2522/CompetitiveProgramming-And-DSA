# Selection Sort

- Time Complexity:
    - Worst Case: O(n^2) = O(n) x O(n) x O(1)

- Space Complexity: O(1)

```c++
for(int i=0 ; i<n-1 ; i++){
    int min = i;
    for(int j=i+1 ; j<n ; j++){
        if(arr[min] > arr[j]){
            min = j;
        }
    }
    if(i != min){
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}
```
