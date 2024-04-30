
/*
https://leetcode.com/problems/valid-palindrome/submissions/1245129975/
*/ 
#include<iostream>
#include <_ctype.h>
#include <string>

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size();

        while (left <right){
                if (!isalnum(s[left])){
                    left++;
                    continue;
                }
                if (!isalnum(s[right])){
                    right--;
                    continue;
                }
                if (tolower(s[left]) == tolower(s[right])){
                    right-=1;
                    left+=1;

                }
                else{
                    return false;
                }
        }
        return true;
    }
};