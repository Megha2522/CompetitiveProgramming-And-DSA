# [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150)

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        int i = 0 , j = numbers.size()-1;

        vector<int>v;

        while(i<j) {
            if(numbers[i] + numbers[j] < target) i++;
            else if(numbers[i] + numbers[j] > target) j--;
            else {
                v.push_back(i+1);
                v.push_back(j+1);
                break;
            }
        }
        return v;
    }
};
```