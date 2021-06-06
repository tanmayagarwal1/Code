import heapq
def MediaEncoderheap(arr):
    if len(arr) == 0:
        return -1 
    q, count, a, b= [], 0, 0, 0
    for i in arr:
        heapq.heappush(q, i)
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        temp = a + b 
        count += temp 
        heapq.heappush(q, temp)
    return count

def MediaEncoder(arr):
	if not arr:
		return 0 
	elif len(arr) == 1:
		return arr[0] 
	dp, index, length = [0 for _ in range(len(arr))], 0, len(arr)
	dp[0] = arr[0]
	for _ in range(length):
		if len(arr) > 1:
			x = min(arr)
			arr.remove(x)
			y = min(arr)
			arr.remove(y)
			dp[index] = x + y
			arr.append(x + y)
			index += 1
	return sum(dp) 


def MediaEncoderWithRecur(arr):
	if len(arr) <= 1:
		return 0 
	a = min(arr)
	arr.remove(a)
	b = min(arr)
	arr.remove(b)
	arr.append(a + b)
	return a + b + MediaEncoderWithRecur(arr)

arr = [4, 8, 6, 12]
print(MediaEncoderWithRecur(arr))

