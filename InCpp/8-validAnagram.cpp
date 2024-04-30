//https://leetcode.com/problems/valid-anagram/submissions/1245968151/
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> sm = {};
        map<char, int>tm = {};
        for(int i = 0;i <s.size();i++){
            if(sm.count(s[i]) ==0){
                sm[s[i]] = 1;
            }else{
                sm[s[i]]+=1;
            }

        }
        for(int i =0;i<t.size();i++){
            if(tm.count(t[i])==0){
                tm[t[i]] =1;
            }else{
                tm[t[i]]+=1;
            }
        }
        if(sm != tm){
            return false;
        }else{
            return true;
        }

    }
};