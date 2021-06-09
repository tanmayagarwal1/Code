import heapq
def AmazonBuilder(arr):
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


print(AmazonBuilder([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
