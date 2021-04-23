import numpy as np 
cumm_run=np.maximum.accumulate
def water_collector(height):
	a=np.array(height)
	global_max=np.argmax(a)
	return int(np.sum(cumm_run(a[:global_max])-a[:global_max],dtype=np.int64)+\
			np.sum(cumm_run(a[:global_max:-1])-a[:global_max:-1],dtype=np.int64))

	
print(water_collector([0,1,0,2,1,0,1,3,2,1,2,1]))