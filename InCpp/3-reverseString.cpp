
/*
https://leetcode.com/problems/reverse-string/submissions/1245133357/
*/

class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0;
        int right = s.size()-1;
        while (left<right){
            char temp;
            temp= s[left];
            s[left] = s[right];
            s[right] = temp;
            left+=1;
            right-=1;
        }
      
    }
};