'''
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
'''

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        appearsOnce = set()
        appearsMore = set()
        maxSeen = -1
        for num in nums:
            if num in appearsOnce:
                appearsOnce.remove(num)
                appearsMore.add(num)
            elif not num in appearsOnce and not num in appearsMore:
                appearsOnce.add(num)
        if appearsOnce:
            return max(appearsOnce)
        return maxSeen