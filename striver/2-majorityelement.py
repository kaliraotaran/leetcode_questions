

'''
https://www.codingninjas.com/studio/problems/majority-element-ii_893027?topList=striver-sde-sheet-problems&problemListRedirection=true&leftPanelTabValue=SUBMISSION

'''

from math import *
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	# Write your code here.
	floor = len(arr)//3
	hash1 = {}
	for i in arr:
		if i not in hash1:
			hash1[i] = 1
		else:
			if i in hash1:
				hash1[i] +=1
	listt =[]
	for keys, values in hash1.items():
		if values>floor :
			listt.append(keys)
	return listt