# Merge Sort

- Time Complexity:
    - Worst Case: O(nlog(n))

- Space Complexity:  O(n)

```c++
#include <bits/stdc++.h>
using namespace std;

// Merge
void merge(int arr[] , int start1 , int end1 , int start2 , int end2){

    // Copy
    int n1 = end1 - start1 + 1;
    int n2 = end2 - start2 + 1;
    int L[n1];
    int R[n2];
    int i,j;

    for( i=start1 , j=0 ; i<=end1 ; i++ , j++){
        L[j] = arr[i];
    }

     for( i=start2 , j=0 ; i<=end2 ; i++ , j++){
        R[j] = arr[i];
    }

    // iterate,compare
    int x = 0; 
    int y = 0;

    // Until both left & right have some data
    while(x < n1 && y < n2){
        if(L[x] > R[y])
            arr[start1++] = R[y++];
        else
            arr[start1++] = L[x++];
    }

    // if some data is remaining in either of left or right
    while(x < n1) arr[start1++] = L[x++];
    while(y < n2) arr[start1++] = R[y++];

    return;
}

// Divide
void divide(int arr[] , int start , int end){

    //Base condition
    if(start >= end) return;

    int mid = start + (end -start)/2;
    divide(arr , start , mid);
    divide(arr , mid+1 , end);    
    merge(arr , start , mid , mid+1 , end);
}

int main(){

    int arr[] = { 2, 27, 4, 3, 8, 17, 0 , -1 , -8 , -10};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Array: ";
    for(auto k: arr) cout << k << " ";
    
    cout << endl;

    divide(arr, 0, n - 1);

    cout << "Sorted Array: ";
    for(auto k: arr) cout << k << " ";

    return 0;
}
```