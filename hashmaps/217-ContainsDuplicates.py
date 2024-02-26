


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dictt = {}
        for i in nums:
            if i not in dictt:
               dictt[i] = 1
            else:
                if i in dictt:
                    dictt[i]+=1
        for  value in dictt.values():
            if value >=2:
                return True
        return False



       
       