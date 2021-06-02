def MergedIntervals(intervals):
	x, merged = sorted(intervals), []
	for i in intervals:
		if not merged or merged[-1][1] < i[0]:
			merged.append(i)
		else:
			merged[-1][1] = max(merged[-1][1], i[1])
	return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(MergedIntervals(intervals))

def NewInterval(intervals, new_interval):
	intervals, merged, flag = sorted(intervals), [], 0
	for i in intervals:
		if i[1] >= newInterval[0]:
			i[1] = max(i[1], newInterval[1])
			i[0] = min(i[0], newInterval[0])
			flag = 1
			break 
	if not flag : intervals.append(newInterval)
	intervals = sorted(intervals)
	for i in range(len(intervals)):
		if not merged or merged[-1][1] < intervals[i][0]:
			merged.append(intervals[i])
		else:
			merged[-1][1] = max(merged[-1][1], intervals[i][1])
	return merged


	
intervals = [[1, 5]]
newInterval = [0, 3]
print(NewInterval(intervals, newInterval))
