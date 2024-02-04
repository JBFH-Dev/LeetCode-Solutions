'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        countAtIndex = {0: -1}
        maxLen = count = 0
        valueMap = {0: -1, 1: 1}
        for end in range(len(nums)):
            count += valueMap[nums[end]]
            if count in countAtIndex:
                maxLen = max(maxLen, end-countAtIndex[count])
            else:
                countAtIndex[count] = end
        return maxLen