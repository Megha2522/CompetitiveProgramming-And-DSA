# [A. Helpful Maths](https://codeforces.com/contest/339/problem/A)

```java
#include <iostream>
using namespace std;

int main() {

    string s;
    cin>>s;
    int l;
    l=s.size();
    for(int j=0;j<l-1;j++){
        for(int i=0;i<l-j-1;i+=2){
            int temp;
            if(s[i]>s[i+2]){
                temp=s[i];
                s[i]=s[i+2];
                s[i+2]=temp;
            }
        }
    }
    cout<<s;
    return 0;
}
```