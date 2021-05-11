def subsets(arr):
    n=len(arr)
    upper_bound = 1<<n

    my_substes = [[arr[i] for i in range(n) if bits & 1<<i != 0] for bits in range(upper_bound)]
    return my_substes

def subsets(arr, type = 2):
    n=len(arr)
    my_subsets = [[]]
    for i in arr:
        my_subsets += [current + [i] for current in my_subsets]
    return my_subsets
print(subsets([1,2,3],type = 2))
