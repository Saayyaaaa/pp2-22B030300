def mini_max_sum(iterable):
    iterable = sorted(iterable)
    return (sum(iterable[:4])), (sum(iterable[:-4]))

minSum, maxSum = mini_max_sum([1,3,5,7,9])
print(f"Minimum sum is {minSum}\nMaximum sum is {maxSum}")