from functools import reduce

def multiply(nums):
    return reduce(lambda x, y: x * y, nums)

list = [2, 3, 4, 5, 6, 7]
print(multiply(list))