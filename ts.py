def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for first in nums:
        for second in nums:
            if (first + second) == target and first != second:
                nums = [first, second]
                return nums

nums = [1,3,5,6]
target = 11
print (twoSum(nums,target))