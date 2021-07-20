from collections import defaultdict
def UsersActiveMinutes(logs, k):
	if not logs : raise ValueError 
	id_dict = dict()
	for id, time in logs:
		if id not in id_dict:
			id_dict[id] = set()
		id_dict[id].add(time)
	res = [0] * k 
	for item in id_dict:
		res[len(id_dict[item]) - 1] += 1
	return res  



logs = [[1,1],[2,2],[2,3]]
k = 4
print(UsersActiveMinutes(logs, k))
