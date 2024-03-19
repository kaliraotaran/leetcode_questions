
'''
https://www.codingninjas.com/studio/problems/sum-of-three-stacks_981318?interviewProblemRedirection=true&leftPanelTabValue=SUBMISSION

the main idea here is that there are 2 stacks that are given and we have to find the max sum of the 3 stacks
that are equal, they teh sum of the 3 stacks are not equal then remove the top elements from those particular stacks

'''

from os import *
from sys import *
from collections import *
from math import *

def sumThreeStacks(vectorA, vectorB, vectorC, lenA, lenB, lenC):

	# Write your code here
	# Return maximum equal stack sum 
	S1 = sum(vectorA)
	S2 = sum(vectorB)
	S3 = sum(vectorC)

	i =0 
	j =0
	k =0 
	ans =0 
	while S1 != S2 or S1 !=S3:
		if i == len(vectorA) or j == len(vectorB) or k ==len(vectorC):
			return 0
		if S1>= S2 and S1>= S3:
			S1-=vectorA[i]
			i+=1
		elif S2 >= S1 and S2 >= S3:
			S2-=vectorB[j]
			j+=1
		else:
			S3 -= vectorC[k]
			k+=1
	return S1