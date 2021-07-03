from scipy import spatial
def KCLosestToOrign(points, k):
	tree = spatial.KDTree(points)
	distance, idx = tree.query(x = [0, 0], k = k, p = 2)
	return [points[i] for i in idx] if k > 1 else [points[idx]]

points =[[3,3],[5,-1],[-2,4]]
k = 2
print(KCLosestToOrign(points, k))