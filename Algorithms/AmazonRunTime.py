def AmazonRunTime(RideDuration, SongDuration):
	if not SongDuration:
		return 0
	time_required, res = RideDuration - 30, []
	SongDuration.sort()
	for i in range(len(SongDuration)):
		for j in range(i + 1, len(SongDuration)):
			if SongDuration[i] + SongDuration[j] == time_required:
				res.append(i)
				res.append(j)
	if not res : return [-1, -1]
	else: return res

time = 90
arr = [1, 10, 25, 35, 60]
print(AmazonRunTime(time, arr))