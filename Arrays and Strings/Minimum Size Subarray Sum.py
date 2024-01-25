'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:    
        curr = 0
        start = 0
        shortest = len(nums) + 1
        for end in range(len(nums)):
            curr += nums[end]
            while curr >= target and start <= end:
                if end - start + 1 < shortest:
                    shortest = end - start + 1
                curr -= nums[start]
                start += 1
        shortest *= (shortest <= len(nums))
        return shortest