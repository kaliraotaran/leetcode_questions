'''
https://leetcode.com/problems/find-common-characters/submissions/1189958063/

we have to return common character in all the different words from the list

we first add the character of the first word to a hashmap

then in a seperate for loop (it loops from the second word to the last)
    we create a new seperate hashmap
    we then iterate through each character of the a word
        if the character was already in the second hashmap and if the number of characters in 
                new hash is less than the num. of characters in teh original hash:
            we then incremnt the value of that character in the hash by 1
    in end of inner loop, we assign the value of new hash to the original hash

    


'''

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        hash1 = defaultdict(int)
        for char in words[0]:
            hash1[char] += 1
        
        for i in range(1, len(words)):
            new_hash = defaultdict(int)
            for char in words[i]:
                if char in hash1 and new_hash[char] < hash1[char]:
                    new_hash[char] += 1
            hash1 = new_hash

        ret = []
        for k in new_hash:
            for _ in range(new_hash[k]):
                ret.append(k)
        
        return ret

