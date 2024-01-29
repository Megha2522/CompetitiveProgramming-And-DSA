# Binary Search

- Time Complexity:
    - Best Case: 
    - Worst Case: 

- Space Complexity: 

```c++
int arr[n] , beg , end , mid , element , flag = 0;  
beg = 0;
end = n-1;
while(beg <= end){
    mid = beg/2 + end/2 ;
    if(arr[mid] == element){
        flag = 1;
        break;
    }
    else if( arr[mid] > element)
    end = mid-1;
    else
    beg = mid+1;
}
if(flag == 1)
cout << "Element found at" << mid ; 
else
cout << "Element not found"; 
```