# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        start = 0
        end = 0
        longest = 0
        zeroes = k
        
        
        # long-winded solution
        currentLen = 0
        while end < len(nums):
            if nums[end] == 1:
                end += 1
                currentLen += 1
            else:
                if zeroes > 0:
                    end += 1
                    currentLen += 1
                    zeroes -= 1
                else:
                    if nums[start] == 0:
                        zeroes += 1
                    start += 1
                    currentLen -= 1
            if currentLen > longest:
                longest = currentLen
                
        if len(nums) == 1:
            if nums[0] or k > 0:
                return 1
            return 0
        
        
        return longest