# O(n) - Time, O(1) - Space

def RabbitHare(arr):
	if len(arr) == 0:
		return -1 
	slow = fast = ans = 0 
	while True:
		slow = arr[slow]
		fast = arr[arr[fast]]
		if slow == fast:
			break  
	while ans != slow:
		ans = arr[ans]
		slow = arr[slow]
	return ans 

arr = [1, 2, 3, 4 ,5, 1, 6]
print(RabbitHare(arr))
