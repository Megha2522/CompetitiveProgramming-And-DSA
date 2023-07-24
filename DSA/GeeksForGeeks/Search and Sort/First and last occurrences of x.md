# [First and last occurrences of x](https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1)

## Using linear Search

```c++
vector<int> find(int arr[], int n , int x )
{
  int firstIndex = -1, lastIndex = -1 , count = 0;
    for(int i=0; i<n ; i++){
        if(arr[i] == x){
            lastIndex = i;
            count++;
        }
    }
    firstIndex = lastIndex-count+1;
    vector<int> answer;
        answer.push_back(firstIndex);
        answer.push_back(lastIndex);
     return answer;
}
```
## Using Binary Search
```c++
vector<int> find(int arr[], int n , int x )
{
    // code here
    int firstIndex = -1 , lastIndex = -1 , count = 0, beg =0 , end = n-1 , mid;
    // first occurence
    while(beg<=end){
        mid = beg +(end - beg)/2;
        
        if(x > arr[mid])
        beg = mid+1;
        else if(x < arr[mid])
        end = mid-1;
        else if(arr[mid] == x){
            firstIndex = mid;
            end = mid-1;
        }
    }
    // last occurence
    beg = 0, end = n-1;
    while(beg<=end){
        mid = beg +(end - beg)/2;
        
        if(x > arr[mid])
        beg = mid+1;
        else if(x < arr[mid])
        end = mid-1;
        else if(arr[mid] == x){
            lastIndex = mid;
            beg = mid+1;
        }
    }
    vector<int> answer;
    answer.push_back(firstIndex);
    answer.push_back(lastIndex);
     return answer;
}
```