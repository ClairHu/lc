# from sys import stdin
# def arrayPairSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     a = 0
#     nums = sorted(nums)
#     print(nums)
#     for n in nums:
#         print("the index of " + str(n) + " is " + str(nums.index(n)))
#         if nums.index(n) % 2 == 0:
#             if nums.index(n) != len(nums)-1:
#                 if nums[nums.index(n) + 1] != n:
#                     a += n
#                 else:
#                     a += n/2
#             else:
#                 a += n
#     print(a)
#     return int(a)


# for line in stdin:
#     nums = [int(x) for x in line.split()]
#     print(nums)
#     arrayPairSum(nums)

# # nums = [1,3,2,5]
# # arrayPairSum(nums)

from sys import stdin
def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    nums = sorted(nums)
    # print(nums)
    for i in range(len(nums)):
        if i % 2 == 0:
            a += nums[i]
    print(a)
    return a


for line in stdin:
    nums = [int(x) for x in line.split()]
    print(nums)
    arrayPairSum(nums)

# nums = [1,3,2,5]
# arrayPairSum(nums)