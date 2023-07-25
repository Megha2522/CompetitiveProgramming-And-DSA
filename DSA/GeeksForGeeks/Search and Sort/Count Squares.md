# [Count Squares](https://practice.geeksforgeeks.org/problems/count-squares3649/1)
```c++
class Solution {
  public:
    int countSquares(int N) {
        // code here
        int len = (int)sqrt(N), ans = 0;
        for(int i = 1 ; i<=len ; i++){
            int square = i*i;
            if(square < N)
            ++ans;
        }
        return ans;
    }
};
```