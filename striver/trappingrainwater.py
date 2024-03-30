'''
https://www.naukri.com/code360/problems/trapping-rainwater_630519?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION
'''


from typing import List

def getTrappedWater(arr: List[int], n: int) -> int:
    # Write your code here.
    trappedwater = 0 
    left =0 
    right = n-1
    leftmax = 0 # this is the max height of the container on the left hand side
    rightmax = 0 # this is teh max height on the right hand sude

    while(left<=right):
        if arr[left] <= arr[right]: # if the wall at the right of the container is longer
            if arr[left]>= leftmax:  # this is if there is a greater value than already that is selected
                leftmax = arr[left]
            else:
                trappedwater += leftmax -arr[left] # here we add the water  which got stuck in between
            left+=1
        else:
            if arr[right]>= rightmax:
                rightmax= arr[right]
            else:
                trappedwater += rightmax -arr[right] # the same thing here,  but with the other side
            right-=1

    return trappedwater