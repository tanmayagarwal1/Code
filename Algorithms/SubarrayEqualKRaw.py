def SubarrayEqualK(arr, k):
	if not arr : return -1 
	pre_sum, ans = [0 for _ in range(len(arr))], 0 
	pre_sum[0] = arr[0]
	for i in range(1, len(arr)):
		pre_sum[i] = arr[i] + pre_sum[i - 1]
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i == 0 :
				local_sum = pre_sum[j]
				if local_sum == k : ans += 1
			else:
				local_sum = pre_sum[j] - pre_sum[i - 1]
				if local_sum == k : ans += 1
	return ans 

arr = [1, 2, 3, 4]
k = 6
print(SubarrayEqualK(arr, k))