# [Find Pair Given Difference](https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1)

```c++
bool findPair(int arr[], int size, int n){
    
    //code
    sort(arr , arr + size);
    for(int i = 0; i  < size; i++ ){
         if(binary_search(arr+i+1,arr+size,n+arr[i])){
             return true;
         }
    }
    return false;
}
```