
/*
https://leetcode.com/problems/container-with-most-water/submissions/1245148639/
*/

class Solution {
public:
    int maxArea(vector<int>& height) {
      int left = 0;
      int right = height.size()-1;
      int maxx= 0;
      
      while (left<right){
            int sum = min(height[left] ,height[right]) *(right-left);
            maxx = max(maxx, sum);
            if (height[left]<height[right]){
                    left++;
            }
            else{

                right-=1;
            }
      }  
      return maxx;
    }
};