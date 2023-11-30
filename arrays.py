#Given an array of integers nums, sort the array in ascending order and return it

def sort_nums(nums):
    sorted_nums = sorted(nums)
    return sorted_nums

input_array =  [23,3,567,8,9,34526,1,56438,17,78,9000000]
sorted_array = sort_nums(input_array)
print(sorted_array)