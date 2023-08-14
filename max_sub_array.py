"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


"""

def max_sub_array(nums:list[int]):
    LagestnoSofar =float('-inf')
    currentSum =0
    for num in nums:
        currentSum += num

        if currentSum > LagestnoSofar:
            LagestnoSofar =currentSum

        if currentSum < 0:
            currentSum=0

    return LagestnoSofar


print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))