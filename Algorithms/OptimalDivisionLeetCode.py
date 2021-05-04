
def optimalDivision(nums):
    res = [str(num) for num in nums]
    if len(res)>2:
        res[1] = '(' + res[1]
        res[-1] = res[-1] + ')'
    return '/'.join(res)
print(optimalDivision([1000,100,10,2]))