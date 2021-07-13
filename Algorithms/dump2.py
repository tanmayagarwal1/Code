from BinaryTreeFull import node, show
import heapq
from math import * 

def IsPairInArr(arr, target):
	if not arr : raise ValueError 
	d = {}
	for i in range(len(arr)):
		if target - arr[i] in d:
			return d[target - arr[i]], i 
		d[arr[i]] = i 
	return - 1

def isMultipleinArr(arr, target):
	if not arr : raise ValueError
	d = {}
	for i in range(len(arr)):
		if target // arr[i] in d and target % arr[i] == 0 :
			return d[target // arr[i]], i 
		d[arr[i]] = i 
	return -1 

def MaximumSubarray(arr, k):
	if not arr:
		raise ValueError 
	r, l, res, prefix = 0, 0, 0, 0
	while r < len(arr):
		prefix += num 
		while l < r and prefix >= k:
			res = max(res, r - l + 1)
			prefix -= arr[l]
			l += 1
		r += 1

	return res 

def MinimumLength(arr, k):
	if not arr : raise ValueError 
	l, r, prefix, res = 0, 0, 0, len(arr) + 1
	while r < len(arr):
		prefix += arr[r]
		while l < r and prefix >= k:
			res = min(res, r - l + 1)
			prefix -= arr[l]
			l += 1
		r += 1
	return res 

def CountSubarryToK(arr, k):
	if not arr : raise ValueError
	d = {0 : 1}
	prefix = 0 
	count = 0 
	for num in arr:
		prefix += num 
		if prefix - k in d:
			count += d[prefix - k ]
		d[prefix] = d.get(prefix, 0) + 1
	return count 

def ReverseStack(arr):
	if not arr : raise ValueError
	tmp = []
	def Helper(arr):
		nonlocal tmp
		if not arr : return 
		tmp.append(arr.pop())
		Helper(arr)
	Helper(arr)
	return tmp 

arr = [1, 2, 3, 4, 5, 6]
print(ReverseStack(arr))






root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)


# root :      20
#            /  \
#           8   22
#          / \    \ 
#         4  12   25
#           /  \
#          10  14


