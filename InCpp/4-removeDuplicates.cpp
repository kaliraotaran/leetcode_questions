
/*
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1245140729/
*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left = 0;
        for(int i =1;i<nums.size();i++){
            if (nums[left]!= nums[i]){
                left+=1;
                nums[left] = nums[i];
            }
            
        }
        return left+1;
    }
};