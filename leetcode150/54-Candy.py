
'''
https://leetcode.com/problems/candy/submissions/1277713595/?envType=study-plan-v2&envId=top-interview-150
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # every child will be given at least one candy
        arr = [1]*len(ratings)
# 2 pass solution

        # first pass
        # increment the candy's based off the left neighbor
        for i in range(1, len(ratings)):
                         # if the left neighbor is less than the current,
                         # then the current deserves one more candy than the prev
             if ratings[i-1]<ratings[i]:
                arr[i] = arr[i-1]+1
        
  # second pass 
        # increment the candy's based off the right neighbor
        for j in range(len(ratings)-2, -1, -1):
                        # if the right neighbor is less than the current,
                        # then current deserves one more candy than the right
            if ratings[j+1]<ratings[j]:
                # if the current indexes candy is already higher than the right then leave it
                # you don't want to update the current candy to candy[right] + 1 because there is a possibility that
                # it will be less than the first pass iteration
                arr[j] = max(arr[j], arr[j+1]+1)
        return sum(arr)
