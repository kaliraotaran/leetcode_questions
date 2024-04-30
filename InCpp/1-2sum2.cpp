
/**
 https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1245123134/
*/
#include<iostream>
#include<vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
       int  left = 0 ;
       int  right = numbers.size()-1;
        int sum = 0;
        while (left<=right){
            sum = numbers[left] + numbers[right];
            if (sum > target)
                right--;
            else if (sum <target)
                left ++;
            else
                return {left+1, right+1}; 

        }
        return {-1, -1};
    }
}; 
