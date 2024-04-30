
//https://leetcode.com/problems/find-the-duplicate-number/submissions/1245949330/
#include<vector>
#include<iostream>
#include <map>
using namespace std;
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        map<int, int> umap = {};
        for (int i =0;i<nums.size();i++){
            if ( umap.count(nums[i])==0){
                umap[nums[i]] =1;
            }else{
                umap[nums[i]]+= 1;
            }
        }
        for(const auto&[key, value]: umap){
            if(value>=2){
                return key;
            }
        }

        return 0;

    }
};