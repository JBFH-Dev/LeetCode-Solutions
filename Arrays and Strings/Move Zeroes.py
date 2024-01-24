'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        counted = 0
        for num in nums:
            if num:
                nums[counted] = num
                counted += 1
        while counted < len(nums):
            nums[counted] = 0
            counted += 1