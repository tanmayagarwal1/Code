def MaximumUnits(boxes, max_truck):
	if not max_truck : raise ValueError 
	boxes.sort(key = lambda x : x[1], reverse = 1)
	res = 0 
	for i, j in boxes:
		i = min(i, max_truck)
		res += i * j 
		max_truck -= i 
		if max_truck <= 0 : break 
	return res 

boxes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(MaximumUnits(boxes, truckSize))
