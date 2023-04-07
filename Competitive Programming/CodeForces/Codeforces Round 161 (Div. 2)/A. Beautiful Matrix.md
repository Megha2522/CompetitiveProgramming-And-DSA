# [A. Beautiful Matrix](https://codeforces.com/contest/263/problem/A)

```java
#include <bits/stdc++.h>
using namespace std;

int main() {
    int m,n;
    for(int i=0;i<5;i++) {
        for(int j=0; j<5; j++) {
            int temp;
            cin >> temp;

            if(temp == 1) {
                m = i;
                n = j;
            }
        }
    }
    int verticalDisp = abs(2-m);
    int horizontalDisp = abs(2-n);
    cout<<verticalDisp + horizontalDisp;
    return 0;
}









 
```