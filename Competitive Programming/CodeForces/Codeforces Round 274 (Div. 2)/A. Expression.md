# [A. Expression](https://codeforces.com/contest/479/problem/A)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {

    int a,b,c,t1,t2,t3,t4,t5,t6;
    cin>>a>>b>>c;
    t1=a+b+c;
    t2=a*b*c;
    t3=(a+b)*c;
    t4=(a*b)+c;
    t5=a*(b+c);
    t6=a+(b*c);
    int arr[]={t1,t2,t3,t4,t5,t6};
     int ans=INT_MIN;
     for(int i=0; i<6 ; i++){
         if(arr[i]>ans){
             ans=arr[i];
         }
     }
    //sort(arr, arr + 5 ,greater<int>());
    cout<<ans;
    return 0;
}
```