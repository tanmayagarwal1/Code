def fourSum(self, nums, target):
    def findNsum(nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results


def founrsum(arr, target):
    def Helper(arr, target, n, path, res):
        if len(arr) < n or n < 2 or target < arr[0] * n or target > arr[-1] * n:
            return 
        if n == 2:
            l, r = 0, len(arr) - 1
            while l < r :
                s = arr[l] + arr[r]
                if s == target:
                    res.append(path + [arr[l], arr[r]])
                    l += 1 
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(arr) - n + 1):
                if i == 0 or (i > 0 and arr[i - 1] != arr[i]):
                    Helper(arr[i + 1:], target - arr[i], n - 1, path + [arr[i]],res)
    res = []
    Helper(sorted(arr), target, 4, [], res)
    return res 

arr = [2,2,2,2,2]
target = 8
print(founrsum(arr, target))