# [A. Even Odds](https://codeforces.com/contest/318/problem/A)

```java
#include <iostream>
using namespace std;

int main() {

    long long n,k;
    cin>>n>>k;

    if(k<=(n+1)/2)
    {
        cout<< (k*2)-1 ;
    }
    else
    {
        if(((k*2)-n)%2==0)
        cout<< (k*2)-n ;
        else
        cout<< (k*2)-n-1;
    }
    return 0;
}
```