#include <map>
#include <vector>

//https://leetcode.com/problems/single-number/submissions/1245964526/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int, int > umap = {};

        for(int i =0;i<nums.size();i++){
            if(umap.count(nums[i]) ==0){
                umap[nums[i]] = 1;
            }else{
                umap[nums[i]]+=1;
            }
        }
        for(const auto& [key,value]:umap){
                if (value==1){
                    return key;
                }
        }
    return 0;
    }
};