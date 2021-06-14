def Scheduler(time, ps):
	res = []
	dp = [0 for _ in range(1441)]
	dpp2 = [0 for _ in range(1441)]
	for i in time:
		for x in range(ToMinutes(i[0]), ToMinutes(i[1])):
			dp[x] = 1
	for i in ps:
		flag = 0 
		for x in range(ToMinutes(i[0]),ToMinutes(i[1])):
			if dp[x] == 1:
				flag = 1
		if flag == 1:
			res.append(False)
			for x in range(ToMinutes(i[0]), ToMinutes(i[1])):
				dp[x] = 1
		else:
			res.append(True)
	return res 


def ToMinutes(time):
	h, m = time.split(':')
	minutes = int(h) * 60 + int(m)
	return minutes % 1440 


schedule  = [["10:00","11:00"],["14:00","16:00"],["23:00","23:30"]]
process = [["11:00","11:30"],["12:00","15:00"],["11:15","13:43"],["17:00","18:40"]]
print(Scheduler(schedule, process))

