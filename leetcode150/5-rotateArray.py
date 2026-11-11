'''
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

here, the simplest approch would be to pop the elements from the end of the array 
and then insert them to the start of the array


'''

class solution:
    def rotate(self, nums):
        ''' this is done in-place, '''
        i =0 
        n = len(nums)
        k = k%n
        while i<k:
            temp = nums.pop()
            nums.insert(0,temp)
            i+=1
        
        # second approach
        # remove elements k times from end of list and then insert at the 0th index

        for i in range(k):
            a = nums.pop()
            nums.insert(0,a)
            

              k = k%len(nums)
        i=0
        j =len(nums)-1
        while i<j:
            nums[i] , nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        ## we have reversed the whole string
        ## now we reverse the first k section
        kl = 0
        kr = k-1
        while kl<=kr:
            nums[kl], nums[kr] = nums[kr], nums[kl]
            kl+=1
            kr-=1
        lk = k
        rk = len(nums)-1
        while lk<rk:
            nums[lk], nums[rk] = nums[rk], nums[lk]
            rk-=1
            lk+=1

            ### we have the think of it as reversing 
            ## the array
            ## first we reverse teh array as is, then we segment
            ## the array into 2 pieces, 0-k, k+1, n
            ##then we reserve those two segments