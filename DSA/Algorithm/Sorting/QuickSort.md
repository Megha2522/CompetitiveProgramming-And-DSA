# [QuickSort]

```c++
#include <bits/stdc++.h>
using namespace std;

int partition(int arr[], int l, int r){
    int pivot = arr[r];
    int t = l - 1;

    for(int i=l;i<r;i++) {
        if(arr[i] < pivot){
            t++;
            swap(arr[t] , arr[i]);
        }
    }

    swap(arr[++t], arr[r]);
    return t;
}

void quickSort(int arr[], int l, int r){

    if(l>=r) return;
    
    int mid = partition(arr, l, r);
    quickSort(arr, l, mid-1);
    quickSort(arr, mid+1, r);
}

int main(){

    int arr[] = { 2, 27, 4, 3, 8, 17, 0 , -1 , -8 , -10};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Array: ";
    for(auto k: arr) cout << k << " ";
    
    cout << endl;

    quickSort(arr, 0, n - 1);

    cout << "Sorted Array: ";
    for(auto k: arr) cout << k << " ";

    return 0;
}
```