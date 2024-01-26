'''
we gonna first initalize 2 varaiable that are situated at 2 corners of the list(beg and end)
we're gonna keep iterating until the left side is still less than the right side pointer
we add the elements of the list at where the pointers currently are
if their sum is > than targer than means the right pointer needs to be moved left (decremented)
if sum < than target, that means the left value is too small and it need to move to the next greater 
element in the list
if their sum is the needed target, we're gonna return their indexes in the list

'''
class Solution:
    def twosum(self,numbers:list, target: int)->list[int]:
        l = 0
        r= len(numbers)-1

        while l<r:
            cursum = numbers[l]+numbers[r]
            if cursum > target:
                r-=1
            elif cursum <target:
                l+=1
            else:
                return [l+1, r+1]
        return []
sol = Solution()
print(sol.twosum([2,3,5,7,88,11], 12))