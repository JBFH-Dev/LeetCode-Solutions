'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (len(nums)*(len(nums)+1))//2
        addedUp = sum(nums)
        return total - addedUp