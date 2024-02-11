'''
https://leetcode.com/problems/unique-morse-code-words/submissions/1172474377/


there exists morse code for everyletter, we find teh morse equivalent for a word,and the words giveen in the list of words
have almost the same morse code since there can be different combinations that can lead to result looking similar to different
words. now, we're supposed to count the different combinations that we used fo revery words since some words may have teh same 
morse code(but concated together in a different order)

we start by createing a variable 'a' that is a string of all the letters in the alphabet
we then start iterating throught the list of words:
and inside that loop, we iterate through that words that we just picked up from the words list:
    we then add the morse equi. by getting teh index of the letter in the alphabet(from 'a' varaible)
    and add it to a varaible
we then add it to a list

in another loop we iterate throught the list where we add teh result of teh prev. loop:
since there can be duplicated, we add only originals to a list and in the end return the len of that list



'''
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a = 'abcdefghijklmnopqrstuvwxyz'
        p = []
        ans= []
        for i in words:
            b = ''
            for j in i:
                b += morse[a.index(j)]
            p.append(b)
        for i in p:
            if i not in ans:
                ans.append(i)
        return len(ans) 
