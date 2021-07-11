import heapq
def FindPair(arr, k):
    if not arr : raise ValueError 
    d = {}
    for i in range(len(arr)):
        if arr[i] - k in d:
            return d[arr[i] - k], d 
        d[arr[i]] = i 
    return - 1

def FindPairMultiply(arr, k):
    if not arr : raise ValueError
    d = {}
    for i in range(len(arr)):
        if k // arr[i] in d and arr[i] % k == 0 :
            return d[k // arr[i]], i 
        d[arr[i]] = i 
    return -1 

def MaximumLengthSubarrayTotarget(arr, k):
    if not arr : raise ValueError
    prefix = 0 
    res = 0 
    l, r = 0, 0 
    while r < len(arr):
        prefix += arr[r]
        while l < r and prefix >= k:
            res = max(res, r - l + 1)
            prefix -= arr[l]
            l += 1
        r += 1
    return res 

def MinimumLengthSubarrayEqualToTarget(arr, k):
    if not arr : raise ValueError
    prefix = 0 
    res = len(arr) + 1
    l, r = 0, 0 
    while r < len(arr):
        prefix += arr[r]
        while l < r and prefix >= k:
            res = min(res, r - l + 1)
            prefix -= arr[l]
            l += 1
        r += 1
    return res if res != len(arr) + 1 else -1 

def CountKDistinctSubarray(arr, k): # Atmost k - Atmost (k - 1)
    if not arr : raise ValueError
    def Helper(arr, k):
        r, l, count, res = 0, 0, 0, 0
        d = {}
        while r < len(arr): # interate till the end of the array 
            d[arr[r]] = d.get(arr[r], 0) + 1 # count ther fequency 
            if d[arr[r]] == 1 : count += 1
            while l < r and count > k:
                d[arr[l]] -= 1
                if d[arr[l]] == 0 : count -= 1
                l += 1
            res += r - l + 1
            r += 1    
        return res 
    
    return Helper(arr, k) - Helper(arr, k - 1)


def MaxLengthSubarrayDistinct(arr, k):
    if not arr : raise ValueError
    def Helper(arr, k):
        r, l, res, count = 0, 0, 0, 0
        d = {}
        while r  < len(arr):
            d[arr[r]] = d.get(arr[r], 0) + 1
            if d[arr[r]] == 1 : count += 1
            while l < r and count > k:
                d[arr[l]] -= 1
                if d[arr[l]] == 0 : count -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res 

    return Helper(arr, k) 

def MaxlengthContainsKZeros(arr, k):
    if not arr : raise ValueError 
    def Helper(arr, k):
        r, l, res, count = 0, 0, 0, 0
        while r < len(arr):
            if arr[r] == 0 : count += 1
            while l < r and count > k:
                if arr[l] == 0 : count -= 1
                l += 1
            res += r - l + 1
            r += 1
        return res 
    
    return Helper(arr, k) - Helper(arr, k - 1)

def Permutations(arr):
    def Helper(arr, path, res):
        if not arr:
            res.append(path)
            return 
        for i in range(len(arr)):
            Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)
    
    if not arr : raise ValueError 
    res = []
    Helper(arr, [], res)
    return res 

def DuplicatesInPermutations(arr):
    def Helper(arr, path, res):
        if not arr:
            res.append(path)
            return 
        for i, num in enumerate(arr):
            if i and arr[i] == arr[i - 1]:
                continue 
            Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

    if not arr : raise ValueError 
    res = []
    Helper(arr, [], res)
    return res 

def PermsSquare(arr):
    def issqaure(x):
        return int(x**0.5)**2 == x 

    def Helper(arr, path, res):
        if not arr:
            res.append(path)
            return 
        for i, num in enumerate(arr):
            if i and arr[i] == arr[i - 1]:
                continue 
            if path and not issqaure(path[-1] + arr[i]):
                continue 
            Helper(arr[:i] + arr[i + 1:], path + [arr[i]], res)

    if not arr:
        raise ValueError 
    res = []
    Helper(arr, [], res)
    return res 

def BeautifulArrangement(n):
    def Helper(arr, path, res, idx):
        if not arr:
            res.append(path)
            return 
        for i, num in enumerate(arr):
            if num % idx == 0 or idx % num == 0 :
                Helper(arr[:i] + arr[i + 1:], path + [arr[i]],res)

    if not n : raise ValueError 
    arr = list(range(1, n + 1))
    Helper(arr, [], path, 1)
    return len(res)

def BA2(n, k):
    if not n : raise ValueError
    arr = list(range(1, n + 1))
    for i in range(1, k):
        arr[i:] = arr[:i - 1 : -1]
    return arr 

def GreyCode(n):
    if not n : raise ValueError 
    res = [0]
    for i in range(1, 2**n):
        res.append(res[-1] ^ (i & ~i + 1))
    return res 



def MonotnoicArray(num):
    if not num : raise ValueError 
    arr = [int(i) for i in num[::-1]]
    idx = -1
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i] or (idx != -1 and arr[i - 1] == arr[i]):
            idx = i 
    if idx == - 1: return num 
    for j in range(idx):
        arr[j] = 9 
    arr[idx] -= 1
    return ''.join([str(i) for i in arr[::-1]])

def InsertParanthsis(n):
    def Helper(Open, Close, path, res):
        if not Open and not Close:
            res.append(path)
            return 
        if Open > 0:
            Helper(Open - 1, Close, path + '(', res)
        if Close > Open:
            Helper(Open, Close - 1, path + ')', res)
    if not n : raise ValueError 
    res = []
    Helper(n, n, '', res)
    return res 

def PascalsTraingle(n):
    if not n : raise ValueError
    res = [1]
    for i in range(n - 1):
        print(res)
        res = [x + y for x, y in zip([0] + res, res + [0])]
    return res 

print(PascalsTraingle(3))


def MountainArray(arr):
    if not arr : raise ValueError 
    res = 0 
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            l, r = i 
            while l and arr[l - 1] < arr[l] : l -= 1
            while r < len(arr) - 1 and arr[r + 1] < arr[r] : r += 1
            res = max(res, r - l + 1)
    return res 

def KminimumWorkers(wages, qual, k):
    if not wages or not qual : raise ValueError 
    expected = sorted([float(w / q), q] for w, q in zip(wage, qual))
    pq = []
    import heapq 
    res = float('inf')
    Qsum = 0 
    for e, q in expected:
        heapq.heappush(pq, -q)
        Qsum += q 
        if len(pq) > k : Qsum += heapq.heappop(pq)
        if len(pq) == k : res = min(res, Qsum * e)
    return res 

def MaximumEfficiency(eff, speed, k):
    if not eff or not speed : raise ValueError
    expected = sorted([e, s] for e, s in zip(eff, speed))
    expected.sort(reverse = True)
    pq = []
    Ssum = 0 
    for e, s in expected:
        heapq.heappush(pq, s)
        Ssum += s 
        if len(pq) > k : Ssum -= heapq.heappop(pq)
        res = max(res, Ssum * e)
    return res 

def KthLargest(arr, k):
    if not arr : raise ValueError 
    def partition(arr, l, h):
        if h < l : return 
        i = l - 1
        pivot = arr[h]
        for x in range(l, h):
            if arr[x] <= pivot:
                i += 1
                arr[x], arr[i] = arr[i], arr[x]
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    def Helper(arr, k):
        if arr:
            mid = partition(arr, 0, len(arr) - 1)
            if k > mid + 1:
                return Helper(arr[mid + 1 :], k - mid - 1)
            elif k < mid + 1:
                return Helper(arr[:mid], k)
            else:
                return arr[mid]
    
    return Helper(arr, len(arr) - k + 1)

def KnearestPointsX(arr, x):
    if not arr : raise ValueError 
    l, h = 0, len(arr) - k 
    while h >= l:
        mid = l + (h - l)//2
        if abs(arr[mid + k] - x) < abs(arr[mid] - x):
            l = mid + 1
        else:
            h = mid - 1
    return arr[l : l + k]

def KClosestToOrigin(arr):
    if not arr : raise ValueError 
    pq = []
    for i, j in arr:
        dist = i * i + j * j 
        heapq.heappush(pq, (-dist, (i, j)))
        if len(pq) > k : heapq.heappop(pq)
    return [i[1] for i in pq]

def Diamonds(arr, k):
    if not arr : raise ValueError 
    Sum = 0 
    pq = []
    for num in arr:
        heapq.heappush(pq, -num)
    count = 0 
    while count < k:
        count += 1
        x = heapq.heappop(pq)
        heapq.heappush(pq, -(-x//2))
        Sum += (-x)
    return Sum 